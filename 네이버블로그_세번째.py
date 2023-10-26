import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 검색어와 검색 페이지 수 설정
search_query = "%EB%A7%A5%EB%B6%81"
max_pages = 100

# 결과를 저장할 Workbook 생성
workbook = Workbook()
sheet = workbook.active

# 엑셀 파일에 헤더 추가
sheet.append(["블로그명", "블로그주소", "글의제목", "날짜"])

for page in range(1, max_pages + 1):
    # 검색 결과 페이지 URL
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_query}&start={str((page-1)*10+1)}"

    # HTTP GET 요청을 보내고 페이지 내용 가져오기
    response = requests.get(url)
    if response.status_code != 200:
        print(f"페이지 {page}를 가져오는 데 문제가 발생했습니다.")
    else:
        # BeautifulSoup을 사용하여 페이지 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 검색 결과 목록 가져오기
        blog_posts = soup.find_all("li", class_="sh_blog_top")

        # 각 블로그 포스트에서 정보 추출
        for post in blog_posts:
            blog_name = post.find("a", class_="sh_blog_title").text
            blog_url = post.find("a", class_="sh_blog_title")["href"]
            post_title = post.find("a", class_="sh_blog_title").attrs.get('title', "")
            post_date = post.find("dd", class_="txt_inline").text

            # 결과를 엑셀 파일에 추가
            sheet.append([blog_name, blog_url, post_title, post_date])

# 결과를 Excel 파일로 저장
workbook.save("c:/work/result.xlsx")

print("결과가 c:/work/result.xlsx 파일로 저장되었습니다.")
