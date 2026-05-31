# 변수 variable
# - 값(literal) 하나를 보관하는 이름 지어진 메모리 공간
a = 10 # a라는 변수(공간)에 10(literal)을 대입해라!
b = '홍길동' # b라는 변수(공간)에 '홍길동' 문자열을 대입해라!

print(a) # 10
print(b) # 홍길동

# 대입 연산자
# - 좌항의 변수(공간)에 우항의 값을 대입해라. 무조건 오른쪽에서 왼쪽으로 대입한다.
num = 100
num = 200
num = a
print(num) # 10

"""
변수명 작성요령
1. 대소문자를 구분한다.
2. 변수명은 snake casing을 사용한다. (단어와 단어사이를 _로 연결)
3. 한글 변수명을 지정할 수 있다. (하지만 인코딩 등의 문제를 야기할 수 있으므로 사용을 지양한다.)
4. 언더바(_)를 제외한 특수문자를 사용할 수 없고, 숫자로 시작할 수 없다.
5. 파이썬 예약어(if, elif, else, for, while, …)를 사용할 수 없다.
6. **직관적인 변수명**을 사용한다. 짧고 간편하다고, a, b, c와 같은 변수명을 사용하지 않는다.
"""
X = 1
x = 11
print(X, x) # 1 11

teamname = '오지라퍼스'
team_name = '오지라퍼스'

팀명 = '오지라퍼스'
print(팀명) # 오지라퍼스

# em@il = 'abc@naver.com'
# 1st_user = '홍길동'
_1st_user = '홍길동'
print(_1st_user)


# 파이썬 예약어
import keyword
print(keyword.kwlist)

user_email = 'abc@naver.com'
price = 100000
print(user_email, price)

# 지나치게 간결한 변수명, 의미를 알수 없는 변수명을 사용하지 말자.
k = True

# 사용자 전화번호

# 사용자 가입일
# user_signup_date
# user_enroll_date
# user_created_at

# 운동선수 키
# player_height

# 상품 원산지
# product_origin

# 주민번호
# ssn
# jumin_no



