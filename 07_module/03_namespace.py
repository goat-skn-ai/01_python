# namespace
# - 변수/함수등을 그룹핑해서 이름충돌을 방지하는 개념
# - module, class, instance등을 namespace로 활용가능

x = 10 # 전역변수

# from skn.my_math import x
# print(x)

from skn import my_math
print(my_math.x)

print(f'x = {x}')

class MyClass:
    x = 33 # 클래스속성
    
    def __init__(self, x):
        self.x = x # 인스턴스 속성

# class 속성 (namespace)
print(MyClass.x)

# instance 속성 (namespace)
my_clz = MyClass(55)
print(my_clz.x)

