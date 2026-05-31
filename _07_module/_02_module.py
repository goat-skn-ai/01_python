# 모듈 module
# - .py 파일을 의미
# - 프로그램내에서 코드 재사용성을 높이기 위해 이 모듈단위로 관리
# - 모듈 하위에 작성된 변수, 함수, 클래스 등은 외부에서 import해 사용할 수 있다.
# - 단, _ 또는 __로 시작하는 이름은 "내부용"이라는 관례가 있으므로 외부 사용을 권장하지 않는다.
# - import * 에서는 _로 시작하는 이름이 제외된다.

import math # 파이썬 내장 모듈 math 가져오기

print("math.pi: ", math.pi)

# dir 빌트인 함수 :특정 모듈의 사용가능한 속성/메소드 나열
print("dir(math): ", dir(math))

print("dir(): ", dir()) # 현재 모듈에서 사용가능한 속성/메소드 나열

# 모듈명 확인
# - import시에는 .py 파일명
# - 현재 모듈을 실행시에는 __main__ 반환
print("math.__name__: " + math.__name__) # math
print("__name__:", __name__)

""" 사용자모듈 가져오기 """
# - 파이썬 패키지로 모듈을 관리
# - 파이썬 패키지 하위의 __init__.py 자동 생성 (지우지 말것)

x = 100
# my_math모듈 namespace로 활용하면서 변수충돌 예방
# from skn import my_math
#
# print("my_math.pi:", my_math.pi)
# print("my_math.x:", my_math.x)
# print("my_math.get_circle_area(10):", my_math.get_circle_area(10))
# print("my_math.__z:", my_math.__z) # 모듈의 __변수는 직접 참조 가능하지만 내부용으로 다룬다.


# from skn.my_math import *
# print("pi:", pi)
# print("x:", x)
# print("get_circle_area(10):", get_circle_area(10))
# print("__z:", __z) # _로 시작하는 내부용 변수는 import *시에는 제외된다.

# 별칭으로 처리
# - from 패키지명 import 모듈명: 특정 패키지에서 모듈을 가져옴
# - from 모듈명 import 함수명/변수명/클래스명: 모듈에서 특정 요소만 가져옴
# - import 모듈명 as 별칭: 모듈을 별칭으로 사용
# - from 패키지명 import 모듈명 as 별칭: 패키지의 모듈을 별칭으로 사용
from skn import my_math as m

print("m.pi (skn.my_math.pi):", m.pi)
print("m.x (skn.my_math.x):", m.x)
print("m.get_circle_area(10):", m.get_circle_area(10))


# (참고) 아래와 같이 모듈명, 메서드명, 변수명 등 이름 충돌을 주의해야 한다.
# str = 'abc'
# print("str(123):", str(123))
#
# import math
# math = 123



# 현재모듈을 실행하는 경우만 하위의 코드를 실행하세요.
# - 현재 모듈을 import해서 사용하는 경우에는 하위의 코드를 실행하지 마세요.
print("__name__: ", __name__)

# __name__: 현재 py 파일의 실행 상태를 알려주는 파이썬 자동 생성 특별 변수
# pass: '아무것도 실행하지 말아라' 키워드

if __name__ == '__main__':
    pass
