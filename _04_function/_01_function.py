# Function 함수
# - 절차적인, 반복적인 실행코드를 가진 자료형.
# - 선언후 호출해서 사용
# - 호출(실행)시에 함수 쪽으로 값을 전달할 수 있고, 결과값을 반환 받을 수 있다.



def add(a, b):
    print(f'a = {a}, b = {b}')
    return a + b

print(add, type(add))
result = add(10, 20)
print(f'result = {result}')

result = add('Hello', 'world')
print(f'result = {result}')

result = add([1, 2, 3], ['🍕', '🍖', '☕'])
print(f'result = {result}')

# 매개변수 | 매개인자(인수)
# - 매개변수 parameter: 함수 선언부의 변수(공간)
# - 매개인자 arguments: 함수 호출부의 전달되는 값

def foo(k, m):
    print(f'k = {k}, m = {m}')

foo(3, 4)
i, j = 10, 20
foo(i, j)

# 리턴값
# - 함수 호출시 함수선언부의 코드실행하고, 이를 마치면 호출부로 반드시 돌아온다. (return)
# - 리턴시에 값하나를 함께 가져올수 있다. (return 선언부가 없으면 None 사용)

def bar():
    print('bar')
    return 0

# print(bar())
# print('🍖🍖🍖')

# 함수는 하나의 값(리터럴)로 처리될 수 있다.
# - 1급시민객체 (값으로써 처리가능한 자료형)
f = bar
f()
print(bar, f, type(f))
print(bar is f)


def runner(f):
    """함수 실행기"""
    f()

runner(bar)

# 호출방식
# 1. 위치 매개인자 전달: 작성한 순서대로 전달
# 2. 키워드 매개인자 전달: key=value에 따라 동일한 이름의 key 매개변수에 전달

def test(a, b):
    print(f'a = {a}, b = {b}')

test(10, 20)
test(a=1, b=2)
test(b=2, a=1)
# test(a=1, b=2, c=3) # TypeError: test() got an unexpected keyword argument 'c'
test(100, b=200) # 혼용하는 경우, 위치 매개인자 - 키워드 매개인자 순으로 작성해야 한다.
# test(b=200, 100) # SyntaxError: positional argument follows keyword argument

# 매개변수 기본값 지정
# - 기본값이 지정된 매개변수는 항상 오른쪽에 위치해야 한다.

# def test2(name, age=20, married): # SyntaxError: parameter without a default follows parameter with a default
def test2(name, age=20, married=False):
    print(f'name = {name}, age = {age}, married = {married}')

test2('홍길동', 33) # 기본값 지정이 안된경우 TypeError: test2() missing 1 required positional argument: 'married'
test2('홍길동', 33, True)
test2('신사임당')

# packing 연산자
# - 반드시 매개변수 또는 좌항에서 사용된다.
# - *args: n개의 위치매개인자가 대입될 매개변수
# - **kwargs: n개의 키워드매개인자가 대입될 매개변수
def test3(*args):
    print(args, type(args))
    return sum(args)

print(test3(1, 2))
print(test3(1, 2, 3, 4, 5))
print(test3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def test4(emoji, *args):
    print(f'emoji = {emoji}, args = {args}')

test4('☕', 1, 2, 3)
test4('☕', 10, 20)
test4('🍖')

def test5(**kwargs):
    print(kwargs, type(kwargs))

test5()
test5(name='윤봉길', age=44, hobby=['축구', '풋볼', '사커'])


def test6(name, age, **kwargs):
    print(name, age, kwargs, type(kwargs))

test6('윤봉길', 44, hobby=['축구', '풋볼', '사커'])

# 매개변수 작성시 유의사항
# - 일반매개변수 - *args - **kwargs
# - 기본값이 있는 매개변수 오른쪽에 작성하면 된다.

def test7(a, b, c, *args, **kwargs):
    print(a, b, c, args, kwargs)

test7(10, 20, 30, 40, 50, name='다비드', age=44)


# unpacking
# - *list: 리스트의 요소를 꺼내어 나열하는 연산자. 매개인자 자리에서 사용
# - **dict: 사전의 요소를 꺼내어 키워드 방식으로 나열하는 연산자. 매개인자 자리에서 사용
names = ['홍길동', '이순신', '유관순']

def test8(*args):
    print(args)

test8(names)
test8(names[0], names[1], names[2])
test8(*names)

info = {"date": "2025/04/14", "time": "16:45"}

def test9(date, time):
    print(date, time)

test9(date='2025/04/14', time='16:45')
test9(date=info['date'], time=info['time'])
test9(**info)

# 위치전용 positional-only, 키워드전용 keyword-only
# / /앞은 위치전용으로만 호출 가능
# * *뒤는 키워드 전용으로만 호출가능
def test10(name, /, greeting="안녕"):
    print(name, greeting)

test10('길동아')
# test10(name='길동') # TypeError: test10() got some positional-only arguments passed as keyword arguments: 'name'

def test11(a, *, b, c):
    print(a, b, c)

# test11(10, 20, 30) # TypeError: test11() takes 1 positional argument but 3 were given
test11(10, b=20, c=30)

# 함수 type-hint
def test12(a: str, b: int) -> str:
    return a + str(b)

print(test12("안녕", 123))
