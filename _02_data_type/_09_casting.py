# 형변환
# - 암묵적 또는 명시적으로 자료형으로 변환하는 것

# 1. 암묵적 형변환
print('--- 암묵적 형변환 ---')
print(1 + 2.3) # int + float -> float + float -> float
print(True + 2) # bool + int -> int + int -> int
print(True + True) # bool + bool -> int + int -> int

# 2. 명시적 형변환
print('--- 명시적 형변환 ---')
# print("안녕" + 123) # TypeError: can only concatenate str (not "int") to str
print("안녕" + str(123)) # "안녕" + "123" -> "안녕123"

height = 175.456
print(int(height)) # 175 (소수점 버림)

value = "1234.567"
print(float(value) * 10)

# 3. 논리형으로의 암묵적 형변환
# - 값이 있으면 True, 값이 0 또는 없으면 False
# - truthy: 조건식에서 True처럼 평가되는 값
# - falsy: 조건식에서 False처럼 평가되는 값
print('--- bool 형변환 - True ---')
print(100, bool(100))
print(-100, bool(-100))
print('abcd', bool('abcd'))
print(' ', bool(' '))
print([1, 2], bool([1, 2]))
print((1, 2), bool((1, 2)))
print({'is_friday': True}, bool({'is_friday': True}))

print('--- bool 형변환 - False ---')
print(0, bool(0))
print(0.0, bool(0.0))
print('', bool(''))
print([], bool([]))
print((), bool(()))
print({}, bool({}))
print(None, bool(None))

# 예시
print('--- bool 형변환 예시 ---')
lst = [1, 2, ]
if lst:
  print('list에 요소가 존재합니다.')
else:
  print('list에 요소가 존재하지 않습니다.')
