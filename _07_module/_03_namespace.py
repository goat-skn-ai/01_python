# namespace
# - 변수/함수등을 그룹핑해서 이름충돌을 방지하는 개념
# - module, class, instance등을 namespace로 활용가능

x = 10 # 전역변수

# from skn.my_math import x
# print("skn.my_math에서 직접 import한 x:", x) # 전역 변수 x가 import한 x로 덮어 씌워짐

from skn import my_math # skn 패키지에서 my_math 모듈 import
print("my_math.x:", my_math.x)

print(f'전역변수 x = {x}')

class MyClass:
    x = 33 # 클래스속성
    
    def __init__(self, x):
        self.x = x # 인스턴스 속성

# class 속성 (namespace)
print("MyClass.x 클래스 속성:", MyClass.x)

# instance 속성 (namespace)
my_clz = MyClass(55)
print("my_clz.x 인스턴스 속성:", my_clz.x)
