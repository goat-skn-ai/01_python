# type(변수명|값) 함수 : 변수나 값의 데이터 타입을 확인하는 내장 함수

# 정수 int
n = 123
print('n:', n, type(n))

# 자릿수 구분 _
price = 123_456_789 # 1억2천....
print('price:', price, type(price))

# 2진법, 8진법 16진법 접두어 및 출력
a = 0b100
print('0b100:', a) # 4
b = 0o23
print('0o23:', b) # 19
c = 0xff
print('0xff:', c) # 255

# 정수 최댓값
import sys
print('sys.maxsize:', sys.maxsize) # 9223372036854775807

# 실수 float
m = 123.456
print('m:', m, type(m))

# 복소수(complex)
c = 3 + 4j
print('c:', c, type(c)) # 3+4j

# 산술연산
print('1 + 2:', 1 + 2)
print('1 - 2:', 1 - 2)
print('1 * 2:', 1 * 2)
print('1 / 2:', 1 / 2)

# 몫
print('10 / 3:', 10 / 3) # 3.3333333333333335
print('10 // 3:', 10 // 3) # 3 (몫)

# 나머지
print('10 % 3:', 10 % 3)


# 거듭제곱
print('3 ** 2:', 3 ** 2)
print('3 ** 3:', 3 ** 3)
