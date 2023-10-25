import re

def validate_korean_id(id_number):
    # 주민등록번호 형식을 정규표현식으로 검사
    pattern = re.compile(r'^\d{6}-[12]\d{6}$')
    if not pattern.match(id_number):
        return False

    # '-'를 기준으로 주민등록번호를 분리
    parts = id_number.split('-')
    birth_date = parts[0]
    gender = parts[1][0]

    # 생년월일 정보 추출
    year = birth_date[:2]
    month = birth_date[2:4]
    day = birth_date[4:6]

    # 성별 정보 확인
    if gender not in ('1', '2'):
        return False

    # 생년월일 유효성 검사
    try:
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        return False

    if year < 0 or month < 1 or month > 12 or day < 1 or day > 31:
        return False

    return True

# 10개의 예제 주민등록번호
sample_ids = [
    '980101-1234567',
    '052502-3234567',
    '071231-1234567',
    '990304-2234567',
    '930512-1234567',
    '900101-1234567',
    '851007-2234567',
    '810201-1234567',
    '020714-2234567',
    '111215-1234567',
]

for id_number in sample_ids:
    is_valid = validate_korean_id(id_number)
    if is_valid:
        print(f'{id_number}은(는) 유효한 주민등록번호입니다.')
    else:
        print(f'{id_number}은(는) 유효하지 않은 주민등록번호입니다.')
