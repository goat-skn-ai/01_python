# dict
# - dictionary 사전 자료형
# - 하나의 요소(item)를 key-value 형식으로 저장
# - 하나의 dict안에 key는 중복될 수 없다.
# - key는 immutable 자료형(int, float, str, tuple)만 가능하다.
# - value는 모든 자료형 가능, 중복가능
# - 저장된 순서를 기억하지 않는다. (key를 통해 value 조회)

dct = {}
dct = {
    'a': 10,
    'b': 20,
    'a': 100 # 중복된 key를 등록하면, 덮어써진다.
}
print(dct, type(dct))

# 요소 조회
print(dct['a'], dct['b'])
key = 'a'
print(dct[key])

# print(dct['c']) # KeyError: 'c'
print(dct.get('a'))
print(dct.get('c')) # 존재하지 않는 key값조회시 기본값 처리 (None)
print(dct.get('c', '값 없음')) # 존재하지 않는 key값조회시 기본값 처리 (None)

# 요소 추가
dct['c'] = 3
dct.update(d=4) # key=value 형식으로 작성
dct.update({'e': 5, 'f': 6})
print(dct)

# 값(value) 제거
dct['f'] = None
print(dct)

# 요소(item) 제거
dct.pop('f')
print(dct)

# dict 내장함수
dct2 = dict(name='홍길동', age=22)
print(dct2)
# key/value로 구성된 tuple을 list로 전달
dct3 = dict([('name', '신사임당'), ('age', 33)])
print(dct3)

# dict api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#dict

# dict.keys()
keys = dct3.keys()
print(keys, type(keys)) # <class 'dict_keys'>

# dict.values()
values = dct3.values()
print(values, type(values)) # <class 'dict_values'>

# dict.items()
items = dct3.items()
print(items, type(items)) # <class 'dict_items'>

# dict 반복순회 (iterable)
for key in dct3:
    print(f'{key} = {dct3[key]}')

for key in dct3.keys():
    print(f'{key} = {dct3[key]}')

for value in dct3.values():
    print(value)

for item in dct3.items():
    print(item, type(item)) # <class 'tuple'>

for key, value in dct3.items():
    print(key, value)

abc = ('A', 'a')
m, n = abc
print(m, n)

# 얕은 복사 (shallow copy) : 특정 객체에 대한 참조주소만 복사
# 깊은 복사 (deep copy) : 특정 객체 내용에 대한 복사
sample = {
    'name': '기계식 키보드',
    'price': 30_000,
    'origin': 'KR',
}

# 얕은복사
other = sample
print(id(sample), id(other))

sample['name'] = '멋진 키보드'
print(other['name'])

# 같은 객체여부 검사
print(sample is other) # True

# 깊은 복사
another = sample.copy()
print(id(sample), id(another))
print(sample is another) # False

sample['price'] *= 10
print(sample)

print(another)


# 리스트 얕은/깊은 복사
prices = [10_000, 20_000, 30_000]

# [얕은 복사] prices의 복사본을 만들어 원본과 동시에 관리
prices_copy = prices
prices.append(40_000)
print(prices_copy)

# [깊은 복사] prices의 복사본을 만들어 각각 10% 값을 올려서 관리 (원본은 변경되면 안됨)
new_prices = prices.copy()
new_prices[0] *= 1.1
new_prices[1] *= 1.1
new_prices[2] *= 1.1
new_prices[3] *= 1.1
print(prices)
print(new_prices)