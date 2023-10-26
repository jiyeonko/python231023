import openpyxl
from openpyxl import Workbook

# 새로운 워크북을 생성하고 기본 시트를 선택합니다.
workbook = Workbook()
sheet = workbook.active

# 헤더 행을 추가합니다.
sheet.append(["ID", "Name", "수량", "가격"])

# 100개의 판매 리스트 행을 생성합니다.
for i in range(1, 101):
    id = i
    name = f"제품{i}"
    수량 = i * 2
    가격 = i * 1000

    # 데이터를 시트에 추가합니다.
    sheet.append([id, name, 수량, 가격])

# 파일을 저장합니다.
workbook.save("c:\\work\\sales.xlsx")

print("sales.xlsx 파일이 생성되었습니다.")
