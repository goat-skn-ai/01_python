# 연산자

## 연산자 우선순위
"""
| 우선순위 | 연산자                         | 설명                                                                          |
|----------|--------------------------------|-----------------------------------------------------------------------------|
| 1        | `()`                           | 괄호 (Grouping)                                                               |
| 2        | `**`                           | 거듭제곱 (Exponentiation)                                                       |
| 3        | `+x`, `-x`, `~x`               | 단항 연산자 (Unary plus, Unary minus, Bitwise NOT)                               |
| 4        | `*`, `/`, `//`, `%`            | 곱셈, 나눗셈, 정수 나눗셈, 나머지 연산 (Multiplication, Division, Floor Division, Modulus) |
| 5        | `+`, `-`                       | 덧셈, 뺄셈 (Addition, Subtraction)                                              |
| 6        | `<<`, `>>`                     | 비트 이동 (Bitwise Shift)                                                       |
| 7        | `&`                            | 비트 AND (Bitwise AND)                                                        |
| 8        | `^`                            | 비트 XOR (Bitwise XOR)                                                        |
| 9        | `|`                                                                           | 비트 OR (Bitwise OR)                                                  |
| 10       | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | 비교 연산자 (Comparisons, Identity, Membership)                                  |
| 11       | `not`                          | 논리 NOT (Logical NOT)                                                        |
| 12       | `and`                          | 논리 AND (Logical AND)                                                        |
| 13       | `or`                           | 논리 OR (Logical OR)                                                          |
| 14       | `if ... else`                  | 조건 표현식 (Conditional Expression)                                             |
| 15       | `lambda`                       | 람다 표현식 (Lambda Expression)                                                  |
| 16       | `:=`                           | 바다코끼리 연산자 (Assignment Expression, walrus operator)
"""

# 삼항연산자
# - [참일때 값] if [조건식] else [거짓일때 값]
# n = int(input('정수를 입력하세요... : ')) # str -> int
# result = '양수' if n > 0 else '음수'
# print(result)

# 사용자의 이름을 입력받아 출력하세요. 작성하지 않은 경우 "이름을 입력해주세요..."라고 출력하세요.
# - {}님, 안녕하세요?
# - 이름을 입력해주세요...
name: str = input('이름 : ')
response: str = f'😊{name}님, 안녕하세요😊' if name else '😡이름을 입력해주세요...😡'
print(response)