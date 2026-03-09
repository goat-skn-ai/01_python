# 조건문 if
# - if : 특정조건에서만 실행되어야 하는 경우(아닌 경우는 아무것도 하지 않음)
#   - 시험점수가 90점 이상인 경우만 커피쿠폰 지급
# - if...else : 모 아니면 도인 경우 (둘 중하나는 무조건 실행되는 경우)
#   - 지금 술을 사려는 고객이 성년인가? 미성년인가?
# - if...elif : 고려해야 하는 조건이 여러가지인 경우(그중 하나만 실행해야 하는 경우)
#   - 학생점수별로 학점 부여

def test1():
    score: int = int(input('시험점수 입력 : '))
    if score >= 90:
        print('☕☕☕ 커피 쿠폰을 드립니다.')

    print('😊수고하셨습니다.😊')

# test1()

def test2():
    score: int = int(input('시험점수 입력 : '))
    if score >= 60:
        print('합격입니다.')
    else:
        print('불합격입니다.')
    print('😊수고하셨습니다.😊')

# test2()

def test3():
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
    if not (score >= 0 and score <= 100):
        raise ValueError('유효한 점수를 입력해주세요...') # 오류 던짐

    # 등급지정
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f'수고하셨습니다. 당신의 점수는 {score}점이고, 등급은 {grade}입니다.')

test3()