# type_hint
# - 파이썬은 동적타이핑을 지원한다.
# - 변수에는 자료형이 없고, 대입되는 리터럴에 따라 자료형이 결정된다.
# - 더 정확히는 변수는 객체를 가리키는 이름이고, 타입은 변수명이 아니라 객체가 가진다.
# - Java처럼 변수 선언 타입이 값을 강제하는 방식과 다르다.
# - 정적 코드 작성시에 타입검사를 수행하는 type_hint를 지원
# - type hint는 IDE와 정적 분석 도구를 돕는 힌트이며, 실제 실행시에는 무시된다.
print('--- 동적 타이핑 ---')
x = '안녕'
x = 123
print(type(x))

print('--- 함수 정의 ---')
def act(x):
    """
    x를 가지고 문자열로 바꿔 xx 함수
    :param x:
    :return:
    """
    print(x)

# type hint
print('--- type hint ---')
greeting: str = 'Hello'
# type hint를 str로 작성했지만, 런타임에서는 int 재대입을 막지 않는다.
greeting = 123
print(greeting)

n: float = 123.456
score: int = 90
has_coupon: bool = True

nums: list[int] = [1, 2, 3]
user: tuple[int, str, str] = (123, '홍길동', 'honggd')
info: dict[str, str | int] = {"name": "신사임당", "age": 42}
chars: set[str] = {'a', 'b', 'c'}

# 상수 표현
# - 파이썬 관례상 대문자로 작성된 변수는 상수로 취급
# - 상수란? 한번 값이 지정되면 바뀌어서는 안되는 변수
# MAX_COUNT = 10
# MAX_COUNT = 5 # 재대입 하면 안됨

from typing import Final

print('--- Final 상수 표현 ---')
MAX_COUNT: Final[int] = 10
# Final 역시 정적 분석 도구를 위한 힌트이며, 파이썬 런타임이 재대입을 직접 막지는 않는다.
MAX_COUNT = 5
print(MAX_COUNT)
