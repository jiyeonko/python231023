import re

# 정규 표현식 패턴 정의
# - \b: 단어 경계를 나타내는 메타 문자. 문자와 공백 사이의 경계를 나타냄.
# - [A-Za-z0-9._%+-]+: 이메일 주소의 로컬 파트 (사용자명) 패턴. 영문 대소문자, 숫자, 특수 문자를 허용.
# - @: "@" 기호
# - [A-Za-z0-9.-]+: 이메일 주소의 도메인 이름. 영문 대소문자, 숫자, 특수 문자를 허용.
# - \.: "." 기호
# - [A-Z|a-z]{2,7}: 최소 2자, 최대 7자까지의 도메인 최상위 수준 도메인 (TLD). 대소문자 알파벳 허용.
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# 이메일 주소가 포함된 텍스트
text = """
이메일 주소 목록:
1. john.doe@example.com
2. alice.smith@subdomain.example.co.uk
3. support@my-website.net
4. not_an_email
5. admin@example.
6. user@.com
7. email@place
8. .com@example
9. johndoe@subdomain
10. user@domainname.domain
"""

# 정규 표현식으로 이메일 주소 검색
# re.findall() 함수를 사용하여 정규 표현식 패턴에 맞는 모든 문자열을 찾아 리스트로 반환
emails = re.findall(pattern, text)

# 찾은 이메일 주소 출력
for email in emails:
    print(email)
