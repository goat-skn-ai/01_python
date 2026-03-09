# for 반복문
# - iterable객체 (str, list, tuple, dict, set)
# - range객체 

name: str = '홍길동'
for ch in name:
    print(ch)

foods: list[str] = ['🍔', '🍖', '🍕']
for food in foods:
    print(food)
    
faces: tuple[str] = ('😊', '😂', '🤣')
for face in faces:
    print(face)

# Any 아무 타입
# object 모든 타입
from typing import Any

user_info: dict[str, Any] = {
# user_info: dict[str, object] = {
    'name': '홍길동',
    'age': 23,
    'hobby': ['독서', '넷플릭스']
}
for k in user_info:
    print(f'{k} = {user_info[k]}')

for k in user_info.keys():
    print(f'{k} = {user_info[k]}')

for k, v in user_info.items():
    print(f'{k} = {v}')

nums: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 짝수만 출력
for num in nums:
    if num % 2 == 0:
        print(num)

# range객체 
# - range(start, end, step=1) 호출시 반환되는 객체
rng: range = range(1, 11)
print(rng)

for n in range(1, 11, 2):
    print(n)

# 1 ~ 10까지 정수의 합
n_sum = 0
for n in range(1, 11):
    # n_sum += n
    n_sum = n_sum + n
print(n_sum)

# 1 ~ 100사이의 홀수의 합
n_sum = 0
for n in range(1, 101, 2):
    n_sum += n
print(f'1 ~ 100사이의 홀수의 합 : {n_sum}')

"""
# 구구단 2단
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6 
2 * 4 = 8 
2 * 5 = 10 
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9 
3 * 4 = 12 
3 * 5 = 15 
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
...

"""
dan = 2
for n in range(1, 10):
    print(f'{dan} * {n} = {dan * n}')


# 중첩반복문
for i in range(2, 10):
    print(f'=== {i}단 ===')
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')

    print()

# 별찍기
"""
행렬구조 
- 행: 바깥반복문의 반복횟수
- 열: 안쪽반복문의 반복횟수
🍕🍕🍕🍕🍕
🍕🍕🍕🍕🍕
🍕🍕🍕🍕🍕
"""

for row in range(0, 3):
    for col in range(0, 5):
        # print(f'({row},{col})', end=' ')
        print(f'🍕', end='')
    print()

print()
# 10행 5열짜리 피자출력
for row in range(0, 10):
    for col in range(0, 5):
        print(f'🍕', end='')
    print()
    
# zip 객체
# - 여러개의 iterable객체를 묶어서 처리
names: list[str] = ['홍길동', '신사임당', '이순신']
scores: list[int] = [88, 95, 56]
data = zip(names, scores)
print(data, type(data))

for name, score in data:
    print(f'{name}: {score}점')

# enumerate 객체
# - 인덱스와 함께 iterable객체 순회 가능
foods: list[str] = ['🍔', '🍖', '🍕']
enum_foods = enumerate(foods)
print(enum_foods, type(enum_foods))

for index, food in enum_foods:
    print(f'{index}: {food}')

# enumerate객체의 순회결과는 인덱스, 요소 2개이다.
for index, (name, score) in enumerate(zip(names, scores)):
    print(f'{index}: {name} : {score}점')


# 평균 점수
scores: list[int] = [100, 99, 50, 34, 67]
score_sum = 0
for score in scores:
    score_sum += score
print(score_sum / len(scores))

# 내장함수 sum
print(sum(scores) / len(scores))


# 학생 list에서 평균점수
students: list[dict[str, object]] = [
    {'name': '홍길동', 'score': 100},
    {'name': '신사임당', 'score': 77},
    {'name': '이순신', 'score': 85},
]

score_sum = 0
for student in students:
    score = student['score']
    score_sum += score

print(round(score_sum / len(students), 2))




