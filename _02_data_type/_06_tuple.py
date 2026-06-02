# tuple
# - 변경불가한(immutable) list
# - 저장순서 기억
# - 주로 데이터의 집합을 안전하게 유지하거나, 함수에서 여러 값을 반환할 때 사용
# - list는 바뀔 수 있는 목록, tuple은 구조가 고정된 값 묶음으로 설명할 수 있다.
# - 예: 학생 정보처럼 계속 수정될 수 있으면 list, RGB값처럼 고정된 묶음은 tuple

print('--- tuple ---')
t1 = () # 빈 tuple
t2 = (10) # 그냥 10과 동일
t3 = (10,) # 튜플 타입으로 인식 시키려면 ,필수
t4 = (10, 20)
t5 = 10, 20 # () 생략 가능
print('t1:', t1, type(t1))
print('t2:', t2, type(t2))
print('t3:', t3, type(t3))
print('t4:', t4, type(t4))
print('t5:', t5, type(t5))

# 읽기전용
# - indexing
# - slicing
print("--- tuple indexing ---")
tpl = ('a', 'b', 'c', 'd')
print('tpl[0] ~ tpl[3]:', tpl[0], tpl[1], tpl[2], tpl[3])
# print(tpl[100]) # IndexError: tuple index out of range

print("--- tuple slicing ---")
print('tpl[1:3]:', tpl[1:3])

# 튜플 값 변경 불가 확인
# tpl[0] = 'A' # TypeError: 'tuple' object does not support item assignment

print('--- tuple unpacking ---')
# tpl_ = 'A', tpl[1], tpl[2], tpl[3]
# tpl_ = 'A', tpl[1:] # ('A', ('b', 'c', 'd'))
tpl_ = 'A', *tpl[1:] # unpacking 연산자
print("('A', *tpl[1:]):", tpl_)

# tuple 활용
# - 복수개의 값을 변수에 할당
# - 값 교환
# a = 100
# b = 200
print("--- tuple 활용: 복수개의 값을 변수에 할당 ---")
a, b = 100, 200
print('a, b:', a, b)

print("--- tuple 활용: 값 교환 ---")
x, y = 88, 99
print('교환 전:', f'x = {x}, y = {y}')
x, y = y, x
print('교환 후:', f'x = {x}, y = {y}')


# 시퀀스 자료형 in 연산: 우항의 시퀀스 자료형에 좌항의 값이 포함되어 있으면 True를 반환
address = '대한민국 서울시 서초구'
print('대한민국' in address)       # True
print('국민한대' in address)       # False
print('서울시서초구' in address)    # False

# 리스트
location = ['서울특별시', '부산광역시', '인천광역시', '광주광역시', '울산광역시']
print('광주광역시' in location)                   # True
print(['광주광역시', '부산광역시'] in location)    # False
print(['서울특별시', '부산광역시'] in location)    # False

# 튜플
nation = ('대한민국', '미국', '중국', '일본', '프랑스')
print('미국' in nation)                 # True
print(('대한민국', '미국') in nation)    # False