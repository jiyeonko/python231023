import requests
from bs4 import BeautifulSoup

# 검색 결과 페이지 URL
url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81"

# HTTP GET 요청을 보내고 페이지 내용 가져오기
response = requests.get(url)
if response.status_code != 200:
    print("페이지를 가져오는 데 문제가 발생했습니다.")
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

        # 결과 출력
        print("블로그명:", blog_name)
        print("블로그 주소:", blog_url)
        print("글의 제목:", post_title)
        print("날짜:", post_date)
        print()

