# match...case
# - 값으로써 분기처리하는 제어문
# - switch...case와 동일(확장)
# - 3.10(2020년) 지원

"""
match 표현식(변수):
    case 값1:
        실행문
    case 값2:
        실행문    
    ...
    case _:
        기본실행문
"""

def test1():
    num = input("음료 선택 (1.콜라 2.사이다 3.쥬스) : ")
    match num:
        case "1":
            print("콜라는 1000원입니다.")
        case "2":
            print("사이다는 1500원입니다.")
        case "3":
            print("쥬스는 2000원입니다.")
        case _:
            print("잘못 입력하셨습니다.")

    print("😊이용해 주셔서 감사합니다.😊")

# test1()

def test2(operand, a, b):
    match operand:
        case '+':
            print(f'{a} + {b} = {a + b}')
        case '-':
            print(f'{a} - {b} = {a - b}')
        case '*':
            print(f'{a} * {b} = {a * b}')
        case '//':
            print(f'{a} // {b} = {a // b}')
        case '%':
            print(f'{a} % {b} = {a % b}')
        case '/':
            print(f'{a} / {b} = {a / b}')
        case _:
            raise ValueError(f"연산자가 부적절합니다.: {operand}")

# test2('+', 10, 3) # 13
# test2('-', 10, 3) # 7
# test2('*', 10, 3) # 30
# test2('//', 10, 3) # 3
# test2('%', 10, 3) # 1
# test2('/', 10, 3) # 3.33333333
# test2('@', 10, 3)

def test3():
    """elif 대체하는 match..case(docstring)"""
    n: int = int(input("정수 입력 : "))
    match n:
        case n if n > 0:
            print('양수를 입력하셨습니다.')
        case n if n < 0:
            print('음수를 입력하셨습니다.')
        case _:
            print('0을 입력하셨습니다.')

# test3()

def test4(value):
    """tuple 값 세부검사"""
    match value:
        case (1, 2):
            print('(1, 2)가 전달되었습니다.')
        case (1, k) if k < 0:
            print('(1, 음수)가 전달되었습니다.')
        case (1, _):
            print('(1, n)가 전달되었습니다.')
        case _:
            print('그 외의 경우')
        
# test4((1, 2))
# test4((1, -10))
# test4((1, 10))
# test4((3, 4))

def test5(applicant):
    """dict의 특정 key값에 세부검사"""
    match applicant:
        case {'type': 'dev', 'career': career} if career >= 10:
            print('중견 개발자 지원입니다.')
        case {'type': 'dev'}:
            print('개발자 지원입니다.')
        case {'type': 'devops'}:
            print('운영/개발자 지원입니다.')
        case _:
            print('기타 지원입니다.')

# test5({'type': 'dev', 'career': 15})
# test5({'type': 'dev', 'career': 5})
# test5({'type': 'devops', 'career': 0})
# test5({'type': 'hr'})


def test6():
    """
    시험점수에 따라 학점등급부여

    점수별 학점 부여
    90 ~ 100: A
    80 ~ 89: B
    70 ~ 79: C
    60 ~ 69: D
    0 ~ 59: F
    """
    score: int = int(input('시험점수 입력: '))
    grade = None

    # 사용자입력값 유효성검사
    if not (0 <= score <= 100): # 체인비교연산자
        raise ValueError('유효한 점수를 입력해주세요...') # 오류 던짐

    # 등급지정
    match score:
        case score if score >= 90:
            grade = 'A'
        case score if score >= 80:
            grade = 'B'
        case score if score >= 70:
            grade = 'C'
        case score if score >= 60:
            grade = 'D'
        case _:
            grade = 'F'

    print(f'수고하셨습니다. 당신의 점수는 {score}점이고, 등급은 {grade}입니다.')

test6()