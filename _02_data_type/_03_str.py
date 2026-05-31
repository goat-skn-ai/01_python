# str (String)
# - 문자열
# - '문자열'  "문자열"  '''문자열'''   """문자열""" 로 감싸서 표현

print("--- 작은 따옴표, 큰 따옴표 ---")
s = '안녕'
s = "안녕"
print(s, type(s))

print("--- 삼중 따옴표 ---")
# 출력되는 문자열 앞/뒤로 엔터 삽입
a = """
문자열 주석 아님. 
그냥 문자열!
"""
print(a)

# 출력되는 문자열 앞/뒤에 엔터 없음
b = """문자열 주석 아님. 
그냥 문자열!"""
print(b)

# 더하기 연산 - 연결
print("--- 더하기 연산(문자열 이어 붙이기) ---")
print('🍕' + '🎃' + '☕')

# 곱하기 연산
print("--- 곱하기 연산(문자열 반복) ---")
print('🍕' * 10)

# 빼기 연산은 불가
# print('🍕' - '🎃') # TypeError: unsupported operand type(s) for -: 'str' and 'str'

# len(객체): 파이썬 객체(문자열, 리스트, 튜플, 딕셔너리, 집합 등) 길이 반환
print('--- len(객체) ---')
text = 'hello'
print(text, len(text))     # hello 5


# str api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#str

print('--- str api ---')

# str.replace(old, new)
# - 특정문자열을 치환해서 새 문자열을 반환
print('--- str.replace() ---')
today = '2026-05-30'
today_ = today.replace('-', '/')
print(today_)

# str.strip([chars])
# - 시작/끝부분 공백 제거
print('--- str.strip() ---')
some = '    하하하 ㅋㅋㅋㅋ    '
print('[', some.strip(), ']')


# 문자열 (문자 + 배열)
# - 인덱스를 통해 접근 가능
# - 0-based index: 0부터 시작, 마지막 인덱스는 (길이-1)
print('--- 문자열 인덱싱 ---')
x = 'Friday'
print('x의 길이:', len(x)) # 길이가 6이므로, 0 ~ 5까지 인덱스를 제공
print(x[0], x[1], x[2], x[3], x[4], x[5])
# print(x[6]) # IndexError: string index out of range

# 역인덱스
print(x[-1], x[-2], x[-3], x[-4], x[-5], x[-6])

# slicing 지원
# - 문자열의 일부를 가져오는 방법
# - [start:stop:step]
# - start 시작하는 인덱스 (inclusive)
# - end 종료 인덱스 (포함되지 않음. exclusive)
# - step 건너뛸 개수 (기본값 1)
print('--- slicing ---')
txt = "hello world"
print('txt: ', txt)
print('txt의 길이: ', len(txt))

print(txt[0:5:1])
print(txt[0:5]) # step 생략시 기본값 1처리
print(txt[:5]) # start 생략시 0번지부터 slicing
print(txt[6:11])
print(txt[6:]) # end 생략시 끝까지 slicing
print(txt[:])
print(txt[::2]) # 0, 2, 4, 6, 8, 10
print(txt[::-1]) # step이 음수인경우 뒤에서부터 가져온다.

# 문자열 불변타입(immutable)
# - 메모리에 할당된 값을 수정할 수 없다.
# - 수정하는 것처럼 보이는 연산은 새 문자열 객체를 만들고, 변수에 다시 대입하는 것이다.
# - int, float, bool, str, tuple은 대표적인 immutable 타입이다.
print('--- 문자열 불변타입 ---')
s = 'hello'
print(id(s)) # 실제 메모리값을 확인
s = s + 'world'
# s += 'world'
print(id(s)) # 메모리값이 변경되었다.

# 멤버쉽 검사 in
# - 포함되었는지 여부
print('--- in ---')
txt = '안녕하세요'
print('안녕' in txt)
print('펭하' in txt)

# 포맷팅
# - 형식문자열의 일부를 다른 변수/값으로 치환
# - %
# - str.format()
# - f-string : 3.6부터 지원
x = 10
y = 3.45

print("--- % 포맷팅 ---")
print('%d + %.2f = %d' % (x, y, x + y)) # %d (decimal)

print("--- format(): 타입 명시 없이 포맷팅 ---")
print('{} + {} = {}'.format(x, y, x + y))

print("--- f-string ---")
print(f'{x} + {y} = {x + y}')

