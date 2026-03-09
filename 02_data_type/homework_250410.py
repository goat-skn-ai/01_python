import math

"""함수 선언"""
def test1():
    n = 123
    print(n)

"""함수 호출(실행)"""
# test1()


def test4():
    """
    0 에서 1 사이의 실수 하나를 입력받아, 소수점 이하가 0.5 이상이면 True를, 그렇지 않으면 False를 출력하시오.
    힌트: round(), 비교연산자 사용
    """
    x = float(input("0 에서 1 사이의 실수 하나를 입력하세요."))
    print(x, round(x)) # 파이썬 0.5, 2.5, ... round 이슈

    print(x - int(x) >= 0.5)




test4()

