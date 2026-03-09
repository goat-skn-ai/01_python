# list
# - 컨테이너 자료형
# - 여러 literal을 묶어서 관리
# - **저장된 순서를 기억**
# - 시퀀스형(str, list, set, tuple)(인덱싱/슬라이싱 가능, 멤버쉽확인 가능)

lst = [1, 2, 3] # 0, 1, 2번지에 값할당
print(lst, type(lst))

print(lst[0], lst[1], lst[2])

# list는 요소를 추가/삭제 가능한 mutable 자료형이다.
print('변경전: ', id(lst))

# 맨뒤에 요소추가
lst.append(4)
print(lst)
print('변경후: ', id(lst))

# 원하는 인덱스 요소추가
lst.insert(1, 1.5)
lst.insert(0, 0)
print(lst)

# 값 변경
lst[0] = -1
print(lst)


# 특정인덱스 값 제거
lst.pop(2)
print(lst)

# 2차원 list
students = [['홍길동', 20], ['신사임당', 22, '여'], ['이순신', 48, '전남', '여수시']]
print(students)

# 인덱싱 (차례대로)
print(students[0])
print(students[0][0])
print(students[1][2])

# csv데이터를 list로 관리
# - Comma Seperated Value (Tab Seperated Value등)
# - "홍길동,20,서울,서초구"
data = "홍길동,20,서울,서초구"
data_ = data.split(',')
print(data_, type(data_))

name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]
print(name, age, addr1, addr2)

# list 반복 순회가능 (iterable형)
lst = ['a', 'b', 'c']
# for 변수 in 순회객체:
for v in lst:
    print(v)

# 인덱스 순회
for index, v in enumerate(lst):
    print(index, v)

# 더하기/곱하기 연산
foods = ['🍔', '🍖']
drinks = ['☕']
print(foods + drinks)
# [['🍔', '🍖'], ['☕']] X
# ['🍔', '🍖', '☕']

print(foods * 3)

# list api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#list

# list.sort() - mutable연산(in-place)
# sorted() - immutable연산(not-in-place)
fruits = ['orange', 'apple', 'banana', 'kiwi']
# fruits.sort()
fruits.sort(reverse=True)
print(fruits)

nums = [20, 25, 10, -10]
# nums.sort()
nums.sort(reverse=True)
print(nums)

# key 정렬기준함수
fruits.sort(key=len)
print(fruits)

# 커스텀 정렬기준함수
def my_sort(elem):
    return len(elem), elem # tuple로 우선순위 지정

fruits.sort(key=my_sort)
print(fruits)

print('list.sort() 반환값: ', fruits.sort()) # None

# sorted를 immutable연산처리
fruits = ['orange', 'apple', 'banana', 'kiwi']
fruits1 = sorted(fruits)
print(fruits)
print(fruits1)

# slicing을 통한 값변경
texts = ['hello', 'hi', '안녕', '곤니찌와']
print(texts[:2], type(texts[:2]))

# texts[:2] = ['ㅋㅋㅋㅋ', '호호호']
texts[1:3] = ['🍖', '🍔']
print(texts)

# 연결연산결과를 기존 list 반영
a = [1, 2]
b = [3, 4]
# a = a + b
a += b
print(a, b)

