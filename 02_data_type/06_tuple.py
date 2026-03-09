# tuple
# - 변경불가한(immutable) list
# - 저장순서 기억

t1 = () # 빈 tuple
# t2 = (10) # 그냥 10과 동일
t2 = (10,) # ,필수
t3 = (10, 20)
t4 = 10, 20
print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))

# 읽기전용
# - indexing
# - slicing
tpl = ('a', 'b', 'c', 'd')
print(tpl[0], tpl[1], tpl[2], tpl[3])
# print(tpl[100]) # IndexError: tuple index out of range
print(tpl[:3])

# tpl[0] = 'A' # TypeError: 'tuple' object does not support item assignment
tpl_ = 'A', tpl[1], tpl[2], tpl[3]
# tpl_ = 'A', tpl[1:] # ('A', ('b', 'c', 'd'))
tpl_ = 'A', *tpl[1:] # unpacking 연산자
print(tpl_)

# tuple 활용
# - 복수개의 값을 변수에 할당
# - 값 교환
# a = 100
# b = 200
a, b = 100, 200
print(a, b)

x, y = 88, 99
print(f'x = {x}, y = {y}')
x, y = y, x
print(f'x = {x}, y = {y}')
