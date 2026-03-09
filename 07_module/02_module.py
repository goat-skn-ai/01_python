# 모듈 module
# - .py 파일을 의미
# - 프로그램내에서 코드 재사용성을 높이기 위해 이 모듈단위로 관리
# - 모듈 하위에 작성된 변수, 함수, 클래스 등은 외부에서 import해 사용할 수 있다.
# - 단, __로 시작하는 private 자원은 외부 사용불가

import math

print(math.pi)

# dir 빌트인 함수 :특정 모듈의 사용가능한 속성/메소드 나열
print(dir(math))

print(dir()) # 현재 모듈에서 사용가능한 속성/메소드 나열

# 모듈명 확인
# - import시에는 .py 파일명
# - 현재 모듈을 실행시에는 __main__ 반환
print(math.__name__) # math
print(__name__)

# 사용자모듈 가져오기
# - 파이썬 패키지로 모듈을 관리
# - 파이썬 패키지 하위의 __init__.py 자동 생성 (지우지 말것)

x = 100

# my_math모듈 namespace로 활용하면서 변수충돌 예방
# from skn import my_math
#
# print(my_math.pi)
# print(my_math.x)
# print(my_math.get_circle_area(10))
# print(my_math.__z) # private변수 직접 참조하면 접근 가능

# from skn.my_math import *
# print(pi)
# print(x)
# print(get_circle_area(10))
# print(__z) # private변수는 import *시에는 제외된다.

# 별칭으로 처리
from skn import my_math as m

print(m.pi)
print(m.x)
print(m.get_circle_area(10))


# 아래와 이름충돌을 주의해야 한다.
# str = 'abc'
# print(str(123))
#
# import math
# math = 123



# 현재모듈을 실행하는 경우만 하위의 코드를 실행하세요.
# - 현재 모듈을 import해서 사용하는 경우에는 하위의 코드를 실행하지 마세요.
if __name__ == '__main__':
    pass