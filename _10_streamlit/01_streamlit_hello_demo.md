# `streamlit hello` 데모 페이지 설명

## 1. `streamlit hello` 명령어란?

`streamlit hello`는 Streamlit을 설치하면 함께 제공되는 공식 데모 앱을 실행하는 명령어이다.

```bash
streamlit hello
```

이 명령어를 실행하면 로컬 Streamlit 서버가 실행되고, 브라우저에서 데모 웹앱이 열린다.

터미널에는 보통 다음과 비슷한 주소가 출력된다.

```text
Local URL: http://localhost:8501
Network URL: http://...
```

브라우저에서는 `http://localhost:8501` 주소로 Streamlit 데모 페이지를 확인할 수 있다.

서버를 종료하려면 터미널에서 다음 키를 누른다.

```text
Ctrl + C
```

## 2. 수업용 핵심 설명

`streamlit hello`는 단순한 "Hello World" 예제가 아니다.

Streamlit으로 만들 수 있는 대표적인 데이터 앱 기능을 한 번에 보여주는 쇼케이스에 가깝다.

수업에서는 다음처럼 설명하면 좋다.

> `streamlit hello`는 Streamlit 설치가 정상적으로 되었는지 확인하면서, Python 코드만으로 웹 화면, 사이드바, 차트, 지도, 데이터프레임을 얼마나 빠르게 만들 수 있는지 보여주는 공식 데모 앱입니다.

## 3. Java/Spring 관점에서 비유

Java/Spring Boot로 웹 화면을 만들려면 보통 다음 요소들이 필요하다.

```text
Controller
Service
Template 또는 Front-end
HTML
CSS
JavaScript
```

반면 Streamlit은 Python 코드 안에서 다음과 같은 명령을 사용해 바로 화면을 만든다.

```python
st.write("Hello Streamlit")
st.button("Click")
st.dataframe(df)
st.line_chart(data)
```

즉, Streamlit은 일반적인 서비스 백엔드 프레임워크라기보다는 **데이터 분석 결과를 빠르게 웹앱으로 보여주는 Python UI 프레임워크**라고 설명하는 것이 좋다.

Spring Boot가 일반 웹서비스를 만드는 데 강하다면, Streamlit은 데이터 분석, AI 모델 결과, 대시보드, 프로토타입을 빠르게 화면으로 보여주는 데 강하다.

## 4. 첫 화면: Welcome to Streamlit

`streamlit hello`를 실행하면 먼저 Streamlit 소개 페이지가 열린다.

이 화면의 핵심 메시지는 다음과 같다.

```text
Python 코드만으로 웹앱 UI를 만들 수 있다.
```

첫 화면에서는 Streamlit이 어떤 도구인지 소개하고, 왼쪽 사이드바에서 여러 데모를 선택할 수 있도록 안내한다.

강의 중에는 다음 포인트를 강조한다.

- Streamlit 앱은 Python 스크립트로 작성한다.
- 실행하면 로컬 웹서버가 뜨고 브라우저에서 확인한다.
- 화면 구성은 `st.write()`, `st.markdown()`, `st.sidebar` 같은 API로 처리한다.
- 데이터 분석 결과를 `print()`로 보는 대신 웹 UI로 보여줄 수 있다.

## 5. 사이드바

데모 페이지 왼쪽에는 사이드바가 있다.

Streamlit에서 사이드바는 다음과 같은 용도로 자주 사용된다.

- 메뉴 선택
- 필터 조건 입력
- 체크박스, 슬라이더, 셀렉트박스 배치
- 대시보드의 옵션 패널 구성

수업에서는 다음처럼 설명할 수 있다.

> 일반 웹앱에서 왼쪽 메뉴나 필터 영역을 따로 HTML/CSS로 만드는 것과 달리, Streamlit에서는 `st.sidebar`를 사용하면 사이드바 UI를 쉽게 만들 수 있습니다.

## 6. Plotting Demo

`Plotting Demo`는 차트와 애니메이션을 보여주는 페이지이다.

이 데모에서는 랜덤 데이터를 계속 생성하면서 선 그래프를 갱신한다.

주요 기능은 다음과 같다.

```python
st.line_chart()
st.progress()
st.button()
```

강의 포인트는 다음과 같다.

- Python에서 생성한 데이터를 바로 차트로 시각화할 수 있다.
- 반복문으로 데이터가 바뀌면 차트도 계속 갱신된다.
- 진행률 표시줄을 통해 작업 진행 상황을 보여줄 수 있다.
- 버튼 클릭으로 앱을 다시 실행하는 흐름을 확인할 수 있다.

학생들에게는 이렇게 설명하면 좋다.

> `Plotting Demo`는 Python 데이터가 Streamlit 화면에서 실시간 차트처럼 표현되는 예제입니다. 데이터 분석 결과를 콘솔에 숫자로만 찍는 것이 아니라, 바로 웹 차트로 보여줄 수 있다는 점을 확인하는 페이지입니다.

## 7. Mapping Demo

`Mapping Demo`는 지도 기반 시각화를 보여주는 페이지이다.

위도, 경도 같은 지리 데이터를 지도 위에 표시하고, 사이드바에서 지도 레이어를 켜고 끄는 식으로 동작한다.

주요 기능은 다음과 같다.

```python
st.pydeck_chart()
st.sidebar.checkbox()
```

강의 포인트는 다음과 같다.

- 지리 좌표 데이터를 지도 위에 시각화할 수 있다.
- 체크박스로 지도 레이어 표시 여부를 제어할 수 있다.
- Streamlit은 차트뿐 아니라 지도 시각화도 지원한다.
- 외부 데이터를 불러오는 예제라 인터넷 연결이 필요할 수 있다.

수업에서는 다음처럼 설명할 수 있다.

> 지도 데이터는 보통 웹에서 구현하려면 지도 라이브러리, 좌표 데이터, JavaScript 설정이 필요합니다. Streamlit은 Python 코드 중심으로 지도 시각화를 빠르게 확인할 수 있게 해줍니다.

## 8. DataFrame Demo

`DataFrame Demo`는 Pandas DataFrame을 Streamlit 화면에 보여주는 예제이다.

단순히 표를 출력하는 것뿐 아니라, 선택한 데이터를 기반으로 차트를 함께 보여준다.

주요 기능은 다음과 같다.

```python
st.write()
st.dataframe()
st.multiselect()
st.altair_chart()
```

강의 포인트는 다음과 같다.

- Pandas DataFrame을 웹 화면의 표로 보여줄 수 있다.
- 사용자가 선택한 값에 따라 표시할 데이터가 달라진다.
- 데이터 표와 차트를 함께 구성할 수 있다.
- 데이터 분석 결과를 대시보드처럼 공유할 수 있다.

학생들에게는 이렇게 설명하면 좋다.

> Jupyter Notebook에서는 분석자가 직접 DataFrame을 확인하는 느낌이라면, Streamlit에서는 다른 사용자도 브라우저에서 데이터를 선택하고 결과를 확인할 수 있는 간단한 데이터 앱으로 바꿀 수 있습니다.

## 9. `streamlit hello`에서 확인할 수 있는 Streamlit 특징

`streamlit hello` 데모를 통해 다음 특징을 확인할 수 있다.

| 특징 | 설명 |
|---|---|
| 빠른 실행 | Python 파일 또는 내장 데모를 명령어 하나로 웹앱 실행 |
| 간단한 UI 작성 | HTML/CSS 없이 `st.*` API로 화면 구성 |
| 데이터 시각화 | 차트, 지도, DataFrame 출력 지원 |
| 인터랙션 | 버튼, 체크박스, 선택박스 등 사용자 입력 처리 |
| 로컬 웹서버 | 실행하면 `localhost:8501`에서 앱 확인 |
| 데이터 앱 특화 | AI, 데이터 분석, 대시보드 프로토타입에 적합 |

## 10. 강의용 설명 흐름

수업에서는 다음 순서로 설명하면 자연스럽다.

### 1단계: 명령어 실행

```bash
streamlit hello
```

설명:

> Streamlit에서 제공하는 공식 데모 앱을 실행하는 명령어입니다. 설치가 잘 되었는지 확인할 때도 사용할 수 있습니다.

### 2단계: 브라우저 확인

설명:

> 터미널에 `Local URL`이 출력되고, 브라우저에서 Streamlit 앱이 열립니다. 이 앱은 내 컴퓨터에서 실행 중인 로컬 웹앱입니다.

### 3단계: 사이드바 확인

설명:

> 왼쪽 사이드바에서 여러 데모를 선택할 수 있습니다. Streamlit에서는 사이드바를 옵션 패널이나 메뉴 영역으로 자주 사용합니다.

### 4단계: 데모별 기능 확인

설명:

> Plotting Demo는 차트, Mapping Demo는 지도, DataFrame Demo는 데이터프레임과 차트를 보여줍니다. Streamlit이 데이터 앱 개발에 필요한 기본 UI를 얼마나 빠르게 제공하는지 확인할 수 있습니다.

### 5단계: 서버 종료

```text
Ctrl + C
```

설명:

> Streamlit 앱은 터미널에서 서버로 실행 중이므로, 종료할 때는 터미널에서 `Ctrl + C`를 누릅니다.

## 11. 한 문장 정리

`streamlit hello`는 Streamlit의 설치 확인용 명령어이면서, Python 코드만으로 차트, 지도, 데이터프레임, 사용자 입력 UI를 가진 데이터 웹앱을 만들 수 있다는 것을 보여주는 공식 데모 앱이다.

## 12. 참고 링크

- [Streamlit CLI 문서](https://docs.streamlit.io/develop/api-reference/cli)
- [Streamlit multipage hello app 설명](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app)
