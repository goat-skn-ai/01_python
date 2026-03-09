# type_hint
# - 파이썬은 동적타이핑을 지원한다.
# - 변수에는 자료형이 없고, 대입되는 리터럴에 따라 자료형이 결정된다.
# - 정적 코드 작성시에 타입검사를 수행하는 type_hint를 지원
# - 실제 실행시에는 무시된다.
x = '안녕'
x = 123
print(type(x))

def act(x):
    """
    x를 가지고 문자열로 바꿔 xx 함수
    :param x:
    :return:
    """
    print(x)

# type hint
greeting: str = 'Hello'
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

MAX_COUNT: Final[int] = 10
MAX_COUNT = 5
print(MAX_COUNT)
