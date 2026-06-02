# 논리형 Boolean
# - bool

print("---논리형 Boolean---")
a = True
b = False

print('a:', a, type(a))
print('b:', b, type(b))

# 비교연산 결과값
print("---비교 연산자---")
# result = (1 > 0.5) # 좌항기준 연산자를 읽어야 한다. gt (greater than)
# result = (1 < 0.5) # lt (less than)
# result = (1 >= 0.5) # ge (greater than or equal to)
# result = (1 <= 0.5) # le (less than or equal to)
# result = (1 == 1) # 동등비교연산자
# result = (1 != 1) # 부정동등비교연산자 (같으면 False, 다르면 True)
# print(result, type(result))

print("1 > 0.5:", 1 > 0.5)
print("1 < 0.5:", 1 < 0.5)
print("1 >= 0.5:", 1 >= 0.5)
print("1 <= 0.5:", 1 <= 0.5)
print("1 == 1:", 1 == 1)
print("1 != 1:", 1 != 1)

print("---논리 부정 연산자 not ---")
print("not a:", not a) # 논리형 반전

# 홀수/짝수
# print("---홀수/짝수---")
# num = int(input('정수를 입력하세요: ')) # 사용자입력(str)을 int 타입으로 변환
# print(num % 2 == 0) # True 짝수 / False 홀수
# print('짝수' if num % 2 == 0 else '홀수') # 삼항연산자 (True일때 값) if (조건식) else (False일때 값)



# and 연산
# - (좌항)과 (우항)이 모두 참일때만 참
# T and T -> T
# T and F -> F
# F and T -> F
# F and F -> F
print('--- and ---')
print("100 > 0 and 1 == 1:", 100 > 0 and 1 == 1) # True
print("30 > 20 and 123 != 123:", 30 > 20 and 123 != 123) # False
print("3 <= -3 and 12 == 12:", 3 <= -3 and 12 == 12) # False
print("9 >= 9 / 9 * 9 and 12 != 11 + 1:", 9 >= 9 / 9 * 9 and 12 != 11 + 1) # False

# or 연산
# - (좌항) 또는 (우항) 하나라도 참이면 참
# T or T -> T
# T or F -> T
# F or T -> T
# F or F -> F
print('--- or ---')
print("100 > 0 or 1 == 1:", 100 > 0 or 1 == 1) # True
print("10 * 10 == 100 or 1 != 1:", 10 * 10 == 100 or 1 != 1) # True
print("100 == 0 or 10 == 10:", 100 == 0 or 10 == 10) # True
print("100 - 1000 > 0 or 23 != 20 + 3:", 100 - 1000 > 0 or 23 != 20 + 3) # False

# 합격여부(과목별 60점이상)
print("--- 합격 또는 불합격 ---")
kor = 70
eng = 65
print('kor, eng:', kor, eng)
print('합격 여부:', '합격' if kor >= 60 and eng >= 60 else '불합격') # 합격 또는 불합격

# 할인대상여부(금일 생일여부, 쿠폰소지여부)
print("--- 할인 가능 또는 불가능 ---")
is_birthday = True
has_coupon = False
print('is_birthday, has_coupon:', is_birthday, has_coupon)
print('할인 여부:', '할인가능' if is_birthday or has_coupon else '할인불가') # 할인가능 또는 할인불가




