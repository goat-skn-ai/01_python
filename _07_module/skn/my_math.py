# 사용자 모듈 작성

pi: float = 3.14

x: int = 20

# __ private 변수 관례: 외부에서 직접 사용하는 것을 권장하지 않는다.
# import * 로 가져올 때는 _로 시작하는 이름이 제외된다.
__z: str = '안뇽'

def get_circle_area(r: float) -> float:
    return r * r * pi

if __name__ == '__main__':
    print('__name__ == "__main__" 여부: my_math.py를 직접 실행했습니다.')
else:
    print("__name__: ", __name__)
    print("다른 모듈에 import skn.my_math가 import 되었습니다.")