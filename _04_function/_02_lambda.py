# lambda 람다
# - 함수를 한줄로 간결히 선언하는 문법
# - lambda x, y: z
# - x, y 매개변수부
# - z 리턴값

# def square(x):
#     return x ** 2

square = lambda x: x ** 2

# print(square(2)) # 4
# print(square(3)) # 9

def test1():
    # return [n ** 2 for n in range(1, 101)]
    # return [square(n) for n in range(1, 101)]
    return [(lambda x: x ** 2)(n) for n in range(1, 101)]

# print(test1())

def test2():
    """하나이상의 매개변수 선언 가능"""
    add = lambda a, b: a + b
    print(add(10, 20))

# test2()

def test3():
    """기본값선언, packing연산자 *args, **kwargs 모두 사용가능"""
    multiply = lambda x, y=1: x * y
    print(multiply(10))
    print(multiply(10, 20))

    adder = lambda *args: sum(args)
    print(adder(1, 2, 3, 4)) # 10
    print(adder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # 55

test3()