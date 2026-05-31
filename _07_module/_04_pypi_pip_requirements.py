# PyPI, pip, requirements.txt
# - PyPI(Python Package Index): Python 외부 패키지를 올리고 내려받는 공식 저장소
# - pip: PyPI 같은 패키지 저장소에서 패키지를 설치/삭제/조회하는 도구
# - requirements.txt: 프로젝트에 필요한 패키지 목록을 적어두는 의존성 명세 파일
#
# Java/Spring 기준으로 비유하면 다음처럼 연결해 설명할 수 있다.
# - PyPI: Maven Central 같은 패키지 저장소
# - pip: Maven/Gradle처럼 의존성을 가져오는 도구
# - requirements.txt: build.gradle 또는 pom.xml의 dependencies 영역과 비슷한 역할
#
# 주의: pip는 설치 도구이고, Maven/Gradle처럼 빌드 라이프사이클 전체를 관리하는 도구는 아니다.
# Python에서는 프로젝트 규모에 따라 pip, venv, requirements.txt, poetry, uv 등을 조합해 사용한다.

# pip install --upgrade pip

# requirements.txt 예시 내용
sample_requirements = """
# 웹 요청 라이브러리
requests==2.32.3

# 환경변수 파일(.env) 로딩
python-dotenv>=1.0.1

# 테스트 도구
pytest~=8.3.0
"""


pip_commands = [
    "python3 -m venv .venv",
    "source .venv/bin/activate",
    "python -m pip --version",
    "python -m pip install requests",
    "python -m pip show requests",
    "python -m pip freeze > requirements.txt",
    "python -m pip install -r requirements.txt",
    "python -m pip uninstall requests",
]


def parse_requirements(requirements_text: str) -> list[str]:
    """requirements.txt 내용에서 실제 패키지 명세만 추출한다."""
    packages = []

    # requirements_text를 한 줄씩 분리(splitlines)하여 반복 처리한다.

    for line in requirements_text.splitlines():
        line = line.strip()   # 각 줄(line)에서 앞뒤 공백을 제거(strip)

        # 빈 줄과 주석은 pip가 설치 대상으로 보지 않는다.
        if not line or line.startswith("#"):
            continue

        # 나머지 실제 패키지 명세 줄만 packages 리스트에 추가
        packages.append(line)

    return packages

packages = parse_requirements(sample_requirements)
print("requirements.txt에서 추출한 설치 대상 패키지:", packages)

print("== 연산자 의미:", "정확히 해당 버전 설치")
print(">= 연산자 의미:", "해당 버전 이상 설치")
print("~= 연산자 의미:", "호환 가능한 최신 패치/마이너 버전 설치")

for command in pip_commands:
    print("수업용 pip 명령어 예시:", command)

print("-" * 50)
if __name__ == "__main__":
    print("__name__ == '__main__' 여부:", "이 파일을 직접 실행했습니다.")
