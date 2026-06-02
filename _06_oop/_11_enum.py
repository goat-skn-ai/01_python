# enum 
# - 상수 모음클래스
# - Enum의 자식클래스로 생성
# - 데이터 타입 첫 수업에서는 심화/보충 주제로 다루고, 객체지향 또는 상수 관리 수업에서 다시 연결하면 좋다.
from enum import Enum

# Gender namespace 하위에 두개의 상수를 정의
print('--- enum 클래스 정의 ---')
class Gender(Enum):
    # 클래스속성으로 name=value 형식으로 지정
    M = '남'
    F = '여'

class Size(Enum):
    S = 0
    M = 1
    L = 2

class Person:
    def __init__(self, name: str, gender: Gender) -> None:
        self.__name = name
        self.__gender = gender

    def __str__(self) -> str:
        return f'Person(name={self.__name}, gender={self.__gender})'

    def get_gender(self):
        return self.__gender


print('--- enum 사용 ---')
hong = Person("홍길동", Gender.M)
sinsa = Person("신사임당", Gender.F)
print(hong)
print(sinsa)

print('--- enum 객체 ---')
print(Gender.M, type(Gender.M))
print(Gender.F, type(Gender.F))

# name/value 속성
print('--- enum name/value ---')
print(Gender.M.name, type(Gender.M.name))
print(Gender.M.value, type(Gender.M.value))

# enum값비교
print('--- enum 비교 ---')
print(hong.get_gender() == Gender.M) # True
print(hong.get_gender() == 'M') # False
print(hong.get_gender().name == 'M') # True

# 순회
print('--- enum 순회 ---')
for gender in Gender:
    print(gender)

# while True:
#     g = input(f"성별을 입력하세요. 1. {Gender.M.value} 2. {Gender.F.value}")
#     print(g)

# 문자열 -> enum
print('--- 문자열 to enum ---')
gender_input = 'M'
gender = Gender[gender_input]
print(gender)

# 사용자입력으로부터 Person객체 생성하기
# name = input("이름 : ")
# gender_input = input("성별 (M/F): ")
# gender = Gender[gender_input]
# person = Person(name, gender)
# print(person)

# enum 각 속성별로 가져오기
print('--- enum members ---')
print(Gender.__members__.keys()) # name
print(Gender.__members__.values()) # value
print(Gender.__members__.items()) # (name, value)
