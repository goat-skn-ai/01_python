# 사용자 모듈 작성

pi: float = 3.14

x: int = 20

# private 변수 : 외부 사용 불가
__z: str = '안뇽'

def get_circle_area(r: float) -> float:
    return r * r * pi

if __name__ == '__main__':
    print('my_math를 실행해 주셔서 감사합니다.')
