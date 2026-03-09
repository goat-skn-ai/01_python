# while 반복문
# - 조건식에 따라 반복횟수가 결정되는 반복문
# - 조건식이 True로 평가되면 반복실행, False로 평가되면 실행중지

# 1 ~ 10까지 출력
# i = 1 # 증감변수 선언 (초기화)
# while i <= 3: # 조건식
#     print(i)
#     i += 1 # 증감식
    
# 무한 반복 케이스
i = 1
while True:
    print(i)
    i += 1

    # 반복문에서 break를 실행하면, 해당 반복문을 즉시 중지한다.
    if i > 10:
        break

print('🍕🍕🍕🍕🍕🍕🍕')

# 사용자 메뉴 주문
menu = """
==============
SK 구내식당 메뉴
==============
1. 된장찌게
2. 비빕밥
3. 김치찌게
0. 종료
==============
선택: """

order: list = []
while True:
    choice = input(menu)
    match choice:
        case '1':
            order.append('된장찌게')
        case '2':
            order.append('비빕밥')
        case '3':
            order.append('김치찌게')
        case '0':
            break # 주문중지
        case _:
            print('잘못 입력하셨습니다.')

print(f'주문내역은 {order}입니다.')