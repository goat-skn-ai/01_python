# Comprehension 내포
# - list comprehension
# - dict comprehension
# - 한줄짜리 반복문을 통해 쉽게 list, dict를 생성하는 방법

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def test1():
    lst: list = []
    for n in range(1, 11):
       lst.append(n)
    return lst

print(test1())

def test2():
    """list 내포"""
    return [n ** 2 for n in range(1, 11)]

print(test2())

def test3():
    """1 ~ 100사이의 짝수만 리스트내포로 생성"""
    # lst: list = []
    # for n in range(1, 101):
    #     if n % 2 == 0:
    #         lst.append(n)
    # return lst
    return [n for n in range(1, 101) if n % 2 == 0]

print(test3())

def test4(lst: list[object]):
    """전달된 list객체에서 정수만 필터링해서 다시 리스트로 반환"""
    return [n for n in lst if isinstance(n, int)]

# isinstance(객체, int) -> bool
print(test4([1, 'ㅋㅋㅋ', 123.456, '🍕', 33, '🤣', 123456, '😡', 0.01234])) # [1, 33, 123456]

print(isinstance(1, int)) # True
print(isinstance('ㅋㅋㅋ', int)) # False

# 중첩반복문
def test5():
    # lst: list[tuple[int, int]] = []
    # for row in range(0, 3): # 0 1 2
    #     for col in range(0, 5): # 0 1 2 3 4
    #         lst.append((row, col))
    # return lst
    return [(row, col) for row in range(0, 3) for col in range(0, 5)]

print(test5())

# dict 내포
def test6():
    """dct = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""
    return {k: k ** 2 for k in range(1, 6)}

print(test6())

def test7(lst: list[str]):
    """주어진 문자열리스트에 대해서 key(문자열): value(문자열)의 길이로 구성된 dict를 반환"""
    return {str: len(str) for str in lst if len(str) >= 3}

print(test7(['hello', 'hi', 'monday', 'ㅋㅋㅋ']))
# {'hello': 5, 'hi': 2, 'monday': 6, 'ㅋㅋㅋ': 3}

# list -> dict 변환
def test8():
    """
    {"홍길동": 33, "신사임당": 24, "논개": 37}
    :return:
    """
    names: list[str] = ['홍길동', '신사임당', '논개']
    ages: list[int] = [33, 24, 37]
    # return {name: age for name, age in zip(names, ages)}
    return dict(zip(names, ages))
print(test8())

# dict -> list(tuple)로 변환
def test9():
    """
    :return:
        names: list[str]
        ages: list[int]
    """
    info: dict[str, int] = {"홍길동": 33, "신사임당": 24, "논개": 37}
    print(info.items())
    print(zip(*info.items())) # * list unpacking -> zip(('홍길동', 33), ('신사임당', 24), ('논개', 37))
    names, ages = zip(*info.items())
    return names, ages

print(test9())
