# 유효범위 Scope
# - 변수에 접근 가능한 범위
# - 전역변수 global variable: 함수블럭 밖에 선언된 변수. 어디서든 접근 가능
# - 지역변수 local variable: 함수블럭 안. 특정 모듈(.py), 특정 함수, 특정 클래스/인스턴스에서 선언된 변수

a = 100 # 전역변수

def foo():
    print("foo()에서 참조한 전역변수 a:", a)

    b = 200 # 지역변수
    print("foo()에서 선언한 지역변수 b:", b)

foo()

# print("foo() 밖에서 지역변수 b:", b) # NameError: name 'b' is not defined
# print("foo.b 함수 객체의 속성 b:", foo.b) # AttributeError: 'function' object has no attribute 'b'

# Python의 for/if 블록은 Java의 중괄호 블록처럼 별도 지역 스코프를 만들지 않는다.
for i in range(3):
    print("for문의 현재 반복 변수 i:", i)

print("for문 종료 후 남아 있는 i:", i) # for문의 i는 전역변수


if True:
    k = 100

print("if 블록에서 선언한 k:", k)

# 우선순위
# - 가깝게 선언된 변수가 우선순위가 높다.
x = 100

def bar():
    # 함수 안에서 같은 이름으로 대입하면 전역 x가 아니라 지역 x가 우선된다.
    x = 200
    print("bar() 안의 지역변수 x:", x)

bar()

# 변수 구분
glo = 10 # 전역
bal = 5 # 전역

def koo(a): # 지역
    glo = a + 10 # 지역 glo
    print("koo() 안의 지역변수 glo:", glo)
    b = a + glo + bal # 지역 b = 지역 a + 지역 glo + 전역 bal
    return b

print("koo(10) 반환값:", koo(10)) # 35
print("koo(10) 호출 후 glo:", glo)
print("koo(bal) 반환값:", koo(bal)) # 25
print("전역변수 bal:", bal) # 5


# call by value | call by reference
# - immutable타입 (int, float, bool, tuple, str) : call by value (값 복사되어 처리)
# - mutable타입 (list, dict, set) : call by reference (참조값이 공유되어 처리)

def func1(a):
    a = 200

a = 100
func1(a)
print("func1(a) 호출 후 immutable 변수 a:", a)

def func2(b):
    b[1] *= 100

b = [1, 2, 3]
func2(b)
print("func2(b) 호출 후 mutable 리스트 b:", b)
