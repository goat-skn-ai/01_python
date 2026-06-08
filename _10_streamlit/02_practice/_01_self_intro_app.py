import streamlit as st


# 실행 명령어:
# streamlit run _01_self_intro_app.py

# 예제 목표:
# - 사용자 입력 위젯으로 값을 입력받는다.
# - 입력된 값을 사용해 화면에 문장을 출력한다.
# - 입력값이 비어 있을 때 안내 메시지를 보여준다.

st.title("자기소개 앱")

st.write("이름, 관심 분야, 오늘의 학습 목표를 입력해 자기소개 문장을 만들어 봅니다.")

# text_input()은 사용자가 직접 문자열을 입력할 수 있는 입력창을 만든다.
name = st.text_input(
    label="이름",
    placeholder="예: 홍길동"
)

# selectbox()는 여러 선택지 중 하나를 고를 수 있는 드롭다운을 만든다.
interest = st.selectbox(
    label="관심 분야",
    options=[
        "Python",
        "데이터 분석",
        "머신러닝",
        "딥러닝",
        "LLM",
        "웹 개발"
    ]
)

goal = st.text_input(
    label="오늘의 학습 목표",
    placeholder="예: Streamlit으로 간단한 앱 만들기"
)

# 입력값이 비어 있으면 완성된 자기소개를 만들 수 없으므로 안내 메시지를 출력한다.
if not name or not goal:
    st.warning("이름과 오늘의 학습 목표를 모두 입력해 주세요.")
else:
    st.success("자기소개 문장이 완성되었습니다.")

    # st.write()는 문자열을 화면에 출력한다.
    # 문자열 안의 Markdown 문법도 일부 적용된다.
    st.write(f"안녕하세요. 저는 **{name}**입니다.")
    st.write(f"저는 **{interest}** 분야에 관심이 있습니다.")
    st.write(f"오늘의 학습 목표는 **{goal}**입니다.")

    # metric()은 대시보드에서 자주 쓰는 핵심 수치 표시 컴포넌트이다.
    # 여기서는 입력 완료 여부를 간단히 시각적으로 보여주기 위해 사용한다.
    st.metric(label="입력 완료 항목", value="3개", delta="완료")
