# 논리형 Boolean
# - bool

a = True
b = False

print(a, type(a))

# 비교연산 결과값
result = (1 > 0.5) # 좌항기준 연산자를 읽어야 한다. gt (greater than)
result = (1 < 0.5) # lt (less than)
result = (1 >= 0.5) # ge (greater than or equal to)
result = (1 <= 0.5) # le (less than or equal to)
result = (1 == 1) # 동등비교연산자
result = (1 != 1) # 부정동등비교연산자 (같으면 False, 다르면 True)
print(result, type(result))

print(not a) # 논리형 반전

# and 연산
# - (좌항)과 (우항)이 모두 참일때만 참
# T and T -> T
# T and F -> F
# F and T -> F
# F and F -> F
print('--- and ---')
print(100 > 0 and 1 == 1)
print(30 > 20 and 123 != 123)
print(3 <= -3 and 12 == 12)
print(9 >= 9 / 9 * 9 and 12 != 11 + 1)

# or 연산
# - (좌항) 또는 (우항) 하나라도 참이면 참
# T or T -> T
# T or F -> T
# F or T -> T
# F or F -> F
print('--- or ---')
print(100 > 0 or 1 == 1)
print(10 * 10 == 100 or 1 != 1)
print(100 == 0 or 10 == 10)
print(100 - 1000 > 0 or 23 != 20 + 3)

# 합격여부(과목별 60점이상)
kor = 70
eng = 65
print('합격' if kor >= 60 and eng >= 60 else '불합격') # 합격 또는 불합격

# 할인대상여부(금일 생일여부, 쿠폰소지여부)
is_birthday = True
has_coupon = False
print('할인가능' if is_birthday or has_coupon else '할인불가') # 할인가능 또는 할인불가






