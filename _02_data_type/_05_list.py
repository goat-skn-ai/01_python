# list
# - 컨테이너 자료형
# - 여러 literal을 묶어서 관리
# - **저장된 순서를 기억**
# - 시퀀스형(str, list, tuple): 저장 순서가 있고 인덱싱/슬라이싱 가능
# - set, dict도 반복 순회(iterable)는 가능하지만, 순서 기반 인덱싱/슬라이싱 대상은 아니다.

print('--- list ---')
lst = [1, 2, 3] # 0, 1, 2번지에 값할당
print('lst:', lst, type(lst)) # [1, 2, 3] <class 'list'>

print('lst[0], lst[1], lst[2]:', lst[0], lst[1], lst[2]) # 1, 2, 3

# list는 요소를 추가/삭제 가능한 mutable 자료형이다.
# - mutable 타입: list, dict, set
# - immutable 타입: int, float, bool, str, tuple
print("--- list mutable check ---")
before_id = id(lst)
print('append 전 id(lst):', before_id)

# 맨뒤에 요소추가
lst.append(4)
print('append 후 lst:', lst) # [1, 2, 3, 4]
print('append 후 id(lst):', id(lst)) # 메모리 주소 일치 == mutable
print('append 전후 같은 객체인가?:', before_id == id(lst))

# 원하는 인덱스 요소추가
print("--- list insert ---")
lst.insert(1, 1.5)
lst.insert(0, 0)
print('insert 후 lst:', lst) # [0, 1, 1.5, 2, 3, 4]

# 값 변경
print("--- list update ---")
lst[0] = -1
print('lst[0] 변경 후 lst:', lst) # [-1, 1, 1.5, 2, 3, 4]


# 특정인덱스 값 제거
print("--- list remove(pop) ---")
removed_value = lst.pop(2)
print('pop(2)로 제거된 값:', removed_value) # 1.5
print('pop 후 lst:', lst) # [-1, 1, 2, 3, 4]

# 2차원 list
print("--- list 2D ---")
students = [
    ['홍길동', 20],
    ['신사임당', 22, '여'],
    ['이순신', 48, '전남', '여수시']
]
print('students 전체:', students)

# 인덱싱 (차례대로)
print("students[0]:", students[0])
print("students[1]:", students[1])
print("students[2]:", students[2])
print("students[0][0]:", students[0][0])
print("students[1][2]:", students[1][2])

# csv데이터를 list로 관리
# - Comma Separated Value (Tab Separated Value등)
# - "홍길동,20,서울,서초구"
print("--- csv data ---")
data = "홍길동,20,서울,서초구"
data_ = data.split(',')
print('split 결과:', data_, type(data_))

name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]
print('분리한 값:', name, age, addr1, addr2)

# list 반복 순회가능 (iterable형)
print("--- list 순회 ---")
lst = ['a', 'b', 'c']
# for 변수 in 순회객체:
for v in lst:
    print('요소:', v)

# 인덱스 순회
print("--- list 인덱스 순회 ---")
for index, v in enumerate(lst):
    print('index:', index, 'value:', v)

# 더하기/곱하기 연산
print("--- list +, * 연산 ---")
foods = ['🍔', '🍖']
drinks = ['☕']
foods_drinks = foods + drinks
print('foods + drinks:', foods_drinks)
# [['🍔', '🍖'], ['☕']] X
# ['🍔', '🍖', '☕']

print('foods * 3:', foods * 3)

# list api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#list

print("--- list api ---")
fruits = ['orange', 'apple', 'banana', 'kiwi', 'apple']
print('fruits:', fruits)

# list.count(value): 리스트 내에 value가 몇 개 있나 카운트
print("fruits.count('apple'):", fruits.count('apple'))


# list.sort() - mutable연산(in-place) == 원본 변환
# sorted() - immutable연산(not-in-place) == 정렬된 새 리스트 반환(원본 유지)

# fruits.sort()
print("--- list.sort() - 원본이 변함 ---")
fruits.sort(reverse=True)
print('fruits.sort(reverse=True) 후 fruits:', fruits)

print("--- list.sort() reverse ---")
nums = [20, 25, 10, -10]
# nums.sort()
nums.sort(reverse=True)
print('nums.sort(reverse=True) 후 nums:', nums)

print("--- list.sort() key ---")
# key 정렬기준함수
fruits.sort(key=len)
print('fruits.sort(key=len) 후 fruits:', fruits)

print("--- list.sort() custom key ---")
# 커스텀 정렬기준함수
def my_sort(elem):
    return len(elem), elem # tuple로 우선순위 지정

fruits.sort(key=my_sort)
print('fruits.sort(key=my_sort) 후 fruits:', fruits)

print('list.sort() 반환값: ', fruits.sort()) # None

# sorted를 immutable연산처리
print("--- sorted - immutable ---")
fruits = ['orange', 'apple', 'banana', 'kiwi']
fruits1 = sorted(fruits)
print('원본 fruits:', fruits)
print('sorted(fruits) 결과:', fruits1)

# slicing을 통한 값변경
print("--- slicing ---")
texts = ['hello', 'hi', '안녕', '곤니찌와']
print('texts: ', texts)
print('texts[:2]: ', texts[:2], type(texts[:2]))

# texts[:2] = ['ㅋㅋㅋㅋ', '호호호']
texts[1:3] = ['🍖', '🍔']
print('slicing 변경 후 texts:', texts) # ['hello', '🍖', '🍔', '곤니찌와']

# 연결연산결과를 기존 list 반영
a = [1, 2]
b = [3, 4]
# a = a + b
a += b
print('a += b 후 a, b:', a, b) # [1, 2, 3, 4] [3, 4]
