# 유효범위 Scope
# - 변수에 접근 가능한 범위
# - 전역변수 global variable: 함수블럭 밖에 선언된 변수. 어디서든 접근 가능
# - 지역변수 local variable: 함수블럭 안. 특정 모듈(.py), 특정 함수, 특정 클래스/인스턴스에서 선언된 변수

a = 100 # 전역변수

def foo():
    print(a) # 전역변수 a

    b = 200
    print(b)

foo()

# print(b) # NameError: name 'b' is not defined
# print(foo.b) # AttributeError: 'function' object has no attribute 'b'

for i in range(3):
    print(i)

print(i)


if True:
    k = 100

print(k)

# 우선순위
# - 가깝게 선언된 변수가 우선순위가 높다.
x = 100

def bar():
    x = 200
    print(x)

bar()

# 변수 구분
glo = 10 # 전역
bal = 5 # 전역

def koo(a): # 지역
    glo = a + 10 # 지역 glo
    b = a + glo + bal # 지역 b = 지역 a + 지역 glo + 전역 bal
    return b

print(koo(10)) # 35
print(koo(bal)) # 25
print(bal) # 5

# call by value | call by reference
# - immutable타입 (int, float, bool, tuple, str) : call by value (값 복사되어 처리)
# - mutable타입 (list, dict, set) : call by reference (참조값이 공유되어 처리)

def func1(a):
    a = 200

a = 100
func1(a)
print(a)

def func2(b):
    b[1] *= 100

b = [1, 2, 3]
func2(b)
print(b)