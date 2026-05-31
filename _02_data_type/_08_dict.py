# dict
# - dictionary 사전 자료형
# - 하나의 요소(item)를 key-value 형식으로 저장
# - 하나의 dict안에 key는 중복될 수 없다.
# - key는 immutable 자료형(int, float, str, tuple)만 가능하다.
# - value는 모든 자료형 가능, 중복가능
# - Python 3.7+ dict는 삽입 순서를 유지한다.
# - 단, list처럼 index가 아니라 key를 통해 value를 조회한다.
# - key는 값을 빠르게 찾기 위한 기준이므로 중간에 값이 바뀌면 안 된다.
# - 그래서 mutable 타입인 list/dict/set은 key로 사용할 수 없다.

print('--- dict ---')
dct = {}
dct = {
    'a': 10,
    'b': 20,
    'a': 100 # 중복된 key를 등록하면, 덮어써진다.
}
print(dct, type(dct))

# key로 사용할 수 있는 타입과 없는 타입
point_map = {
    (10, 20): '서울 좌표'
}
print(point_map[(10, 20)])
# invalid_key_map = {[10, 20]: '서울 좌표'} # TypeError: unhashable type: 'list'

# 요소 조회
print('--- dict 조회 ---')
print(dct['a'], dct['b'])
key = 'a'
print(dct[key])

# print(dct['c']) # KeyError: 'c'
print(dct.get('a'))
print(dct.get('c')) # 존재하지 않는 key값조회시 기본값 처리 (None)
print(dct.get('c', '값 없음')) # 존재하지 않는 key값조회시 기본값 처리 (None)

# 요소 추가
print('--- dict 추가 ---')
dct['c'] = 3
dct.update(d=4) # key=value 형식으로 작성
dct.update({'e': 5, 'f': 6})
print(dct)

# 값(value) 제거
print('--- dict value 제거 ---')
dct['f'] = None
print(dct)

# 요소(item) 제거
print('--- dict item 제거 ---')
dct.pop('f')
print(dct)

# dict 내장함수
print('--- dict 내장함수 ---')
dct2 = dict(name='홍길동', age=22)
print(dct2)
# key/value로 구성된 tuple을 list로 전달
dct3 = dict([('name', '신사임당'), ('age', 33)])
print(dct3)

# dict api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#dict

# dict.keys()
print('--- dict keys ---')
keys = dct3.keys()
print(keys, type(keys)) # <class 'dict_keys'>

# dict.values()
print('--- dict values ---')
values = dct3.values()
print(values, type(values)) # <class 'dict_values'>

# dict.items()
print('--- dict items ---')
items = dct3.items()
print(items, type(items)) # <class 'dict_items'>

# dict 반복순회 (iterable)
print('--- dict 순회 (key만 꺼냄)---')
for key in dct3:
    print(f'{key} = {dct3[key]}')

print('--- dict keys 순회 ---')
for key in dct3.keys():
    print(f'{key} = {dct3[key]}')

print('--- dict values 순회 ---')
for value in dct3.values():
    print(value)

print('--- dict items 순회 ---')
for item in dct3.items():
    print(item, type(item)) # <class 'tuple'>

print('--- dict items unpacking ---')
for key, value in dct3.items():
    print(key, value)

print('--- tuple unpacking ---')
abc = ('A', 'a')
m, n = abc
print(m, n)

# 대입: 같은 객체를 함께 바라보도록 참조주소를 복사
# 얕은 복사 (shallow copy): 새 컨테이너 객체를 만들지만, 내부 중첩 객체는 공유할 수 있다.
# 깊은 복사 (deep copy): 내부 중첩 객체까지 재귀적으로 새로 복사
sample = {
    'name': '기계식 키보드',
    'price': 30_000,
    'origin': 'KR',
}

# 얕은복사
print('--- dict 얕은 복사 ---')
other = sample
print(id(sample), id(other))

sample['name'] = '멋진 키보드'
print(other['name'])

# 같은 객체여부 검사
print(sample is other) # True

# dict.copy()는 새 dict 객체를 만드는 얕은 복사이다.
# 현재 sample처럼 중첩 객체가 없는 단순 dict에서는 깊은 복사처럼 보일 수 있다.
print('--- dict 얕은 복사: copy() ---')
another = sample.copy()
print(id(sample), id(another))
print(sample is another) # False

sample['price'] *= 10
print(sample)

print(another)

# 중첩 객체가 있는 경우 copy()와 deepcopy()의 차이가 드러난다.
print('--- 중첩 dict copy()와 deepcopy() 비교 ---')
import copy

nested_sample = {
    'name': '노트북',
    'options': ['16GB RAM', '512GB SSD']
}

shallow_copy = nested_sample.copy()
deep_copy = copy.deepcopy(nested_sample)

nested_sample['options'].append('외장 그래픽')
print('원본:', nested_sample)
print('copy() 결과:', shallow_copy) # 내부 list를 원본과 공유
print('deepcopy() 결과:', deep_copy) # 내부 list까지 별도 복사


# 리스트 대입/copy() 비교
print('--- list 대입/copy() 비교 ---')
prices = [10_000, 20_000, 30_000]

# [대입] prices와 prices_copy가 같은 list 객체를 함께 바라본다.
prices_copy = prices
prices.append(40_000)
print(prices_copy)

# [copy()] prices의 복사본을 만들어 각각 10% 값을 올려서 관리 (원본은 변경되면 안됨)
new_prices = prices.copy()
new_prices[0] *= 1.1
new_prices[1] *= 1.1
new_prices[2] *= 1.1
new_prices[3] *= 1.1
print(prices)
print(new_prices)
