# pip, requirements.txt, 가상환경 실제 설치 확인 실습
#
# 가상환경(virtual environment)이란?
# - 프로젝트마다 독립된 Python 실행 환경과 패키지 설치 공간을 만들어 주는 기능이다.
# - Java/Spring으로 비유하면 프로젝트별로 Gradle/Maven 의존성을 따로 관리하는 것과 비슷하다.
# - 전역 Python에 패키지를 계속 설치하면 프로젝트 A에서 필요한 버전과 프로젝트 B에서 필요한 버전이
#   충돌할 수 있다. 가상환경을 쓰면 각 프로젝트가 자기만의 site-packages 폴더를 갖는다.
# - 그래서 실무에서는 pip로 패키지를 설치하기 전에 먼저 가상환경을 만들고 활성화하는 흐름을 권장한다.

# (.venv)는 Python이 기본 제공하는 프로젝트별 독립 방이고,
# (base)는 Anaconda가 설치하면서 기본으로 열어 둔 Python 작업방입니다.
#
# cd 01_python/_07_module
#
# 1. 가상환경 생성
#    python3 -m venv .venv
#    또는
#    python -m venv .venv
#
#    설명:
#    - venv는 Python 표준 라이브러리에 포함된 가상환경 생성 도구이다.
#    - .venv는 가상환경 폴더 이름이다. 관례적으로 프로젝트 루트나 실습 폴더에 .venv라는 이름을 많이 쓴다.
#
# 2. 가상환경 활성화
#    macOS/Linux: source .venv/bin/activate
#    Windows    : .venv\Scripts\activate
#
#    설명:
#    - 활성화하면 터미널 프롬프트 앞에 (.venv)처럼 표시된다.
#    - 이 상태에서 python, pip 명령을 실행하면 전역 Python이 아니라 .venv 안의 Python과 pip를 사용한다.
#
#
# 3. requirements.txt 기반 패키지 설치
#    python -m pip install -r requirements.txt
#
# 4. 설치 확인
#    python _05_pip_requirements_practice.py
#
# 5. 현재 환경에 설치된 패키지 목록 확인
#    python -m pip freeze
#
# 6. 가상환경 비활성화
#    deactivate
#
#    설명:
#    - 수업이나 작업이 끝났을 때 현재 터미널에서 가상환경 사용을 종료한다.
#    - 비활성화하면 다시 시스템 기본 Python 환경으로 돌아간다.

# 정리:
# - 가상환경 생성: python -m venv .venv
# - 가상환경 활성화: source .venv/bin/activate 또는 .venv\Scripts\activate
# - 패키지 설치: python -m pip install -r requirements.txt
# - 가상환경 종료: deactivate

from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
from io import StringIO


# 왼쪽은 PyPI 배포 패키지 이름, 오른쪽은 Python 코드에서 import할 때 쓰는 모듈 이름이다.
# 예: python-dotenv는 설치 이름과 import 이름이 다르다.
REQUIRED_PACKAGES = {
    "requests": "requests",
    "colorama": "colorama",
    "python-dotenv": "dotenv",
}


def find_missing_packages() -> list[str]:
    """requirements.txt 패키지가 현재 Python 환경에 설치되어 있는지 확인한다."""
    missing_packages = []

    for package_name in REQUIRED_PACKAGES:
        try:
            version(package_name)
        except PackageNotFoundError:
            missing_packages.append(package_name)

    return missing_packages


def print_installed_versions() -> None:
    """설치된 패키지 버전을 출력한다."""
    for package_name in REQUIRED_PACKAGES:
        print(f"{package_name} 설치 버전:", version(package_name))


def print_import_results() -> None:
    """설치된 패키지를 실제 Python 모듈로 import할 수 있는지 확인한다."""
    for package_name, module_name in REQUIRED_PACKAGES.items():
        import_module(module_name)
        print(f"{package_name} -> {module_name} import 결과:", "성공")


missing_packages = find_missing_packages()

if missing_packages:
    print("설치되지 않은 패키지 목록:", missing_packages)
    print("가상환경 생성 명령:", "python -m venv .venv")
    print("가상환경 활성화 명령(macOS/Linux):", "source .venv/bin/activate")
    print("가상환경 활성화 명령(Windows):", r".venv\Scripts\activate")
    print("패키지 설치 명령:", "python -m pip install -r requirements.txt")
    print("설치 후 확인 명령:", "python _05_pip_requirements_practice.py")
    print("가상환경 비활성화 명령:", "deactivate")
else:
    print("requirements.txt 설치 확인:", "필요한 패키지가 모두 설치되어 있습니다.")
    print_installed_versions()
    print_import_results()

    import requests
    from colorama import Fore, Style
    from dotenv import dotenv_values

    request = requests.Request("GET", "https://example.com/api/students")
    prepared_request = request.prepare()

    print("requests 요청 메서드 예시:", prepared_request.method)
    print("requests 요청 URL 예시:", prepared_request.url)

    print("colorama 색상 문자열 예시:", Fore.GREEN + "설치 확인 성공" + Style.RESET_ALL)

    env_values = dotenv_values(stream=StringIO("APP_NAME=module-class\nDEBUG=true\n"))

    print(".env 문자열 파싱 결과:", dict(env_values))


if __name__ == "__main__":
    print("__name__ == '__main__' 여부:", "이 파일을 직접 실행했습니다.")
