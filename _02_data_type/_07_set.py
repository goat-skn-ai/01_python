# set 집합
# - 중복값을 허용하지 않는다.
# - 반복 순회는 가능하지만, 순서 기반 인덱싱/슬라이싱은 지원하지 않는다.
# - 중복 제거에는 유용하지만, 원래 데이터 순서가 중요하면 주의해야 한다.
# - set api에는 집합관련 연산 (합집합, 교집합, 차집합, 여집합)

print('--- set ---')
st = {2, 3, 2, 3, 1, 2, 3, 4, 3, 2}
print('st:', st, type(st))

# list 중복제거
print('--- set을 이용한 list 중복제거 ---')
lst = [2, 3, 2, 3, 1, 2, 3, 4, 3, 2]
st2 = set(lst)
print('set(lst):', st2)
lst2 = list(st2)
print('list(set(lst)):', lst2)
# 주의: list -> set -> list 변환은 중복을 제거하지만, 원래 순서를 보존하는 용도로 설명하면 안 된다.

# tuple 중복제거
print('--- set을 이용한 tuple 중복제거 ---')
tpl = ('a', 'b', 'b', 'c', 'x', 'c', 'x', 'a')
print('tuple(set(tpl)):', tuple(set(tpl)))

# 요소 추가
print('--- set add ---')
my_nums = {20, 30, 40}
my_nums.add(50)
print('add(50) 후 my_nums:', my_nums)

# 요소 제거
print('--- set remove/discard ---')
my_nums.remove(50) # 삭제하고자 하는 값을 전달
# my_nums.remove(100) # KeyError: 100 존재하지 않는 값을 삭제시 오류
my_nums.discard(100) # 값이 없어도 오류나지 않음
print('remove(50), discard(100) 후 my_nums:', my_nums)

# 반복순회가능 (iterable객체)
print('--- set 순회 ---')
for v in my_nums:
    print('요소:', v)

# 모든 요소 제거
print('--- set clear ---')
my_nums.clear()
print('clear() 후 my_nums:', my_nums)

# 집합연산
print('--- set 집합연산 ---')
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n))
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합
