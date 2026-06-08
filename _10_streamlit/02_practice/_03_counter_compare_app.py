import streamlit as st


# 실행 명령어:
# streamlit run _03_counter_compare_app.py

# 예제 목표:
# - 일반 변수와 st.session_state의 차이를 비교한다.
# - Streamlit은 버튼 클릭 같은 사용자 상호작용이 발생하면 스크립트를 위에서 아래로 다시 실행한다.
# - 그래서 일반 변수는 매번 다시 초기화되고, session_state는 같은 사용자 세션 안에서 값을 유지한다.

st.title("카운터 비교 앱")

st.write("일반 변수 카운터와 Session State 카운터의 차이를 비교해 봅니다.")

left_column, right_column = st.columns(2)

with left_column:
    st.header("일반 변수 카운터")

    # Streamlit은 버튼을 누를 때마다 파일 전체를 다시 실행한다.
    # 따라서 count는 매번 다시 0으로 초기화된다.
    count = 0

    if st.button("일반 변수 +1"):
        count += 1

    st.write("일반 변수 count:", count)
    st.caption("버튼을 여러 번 눌러도 값이 계속 누적되지 않습니다.")

with right_column:
    st.header("Session State 카운터")

    # st.session_state는 같은 사용자 세션에서 유지할 값을 저장하는 공간이다.
    # count 값이 아직 없다면 처음 한 번만 0으로 초기화한다.
    if "count" not in st.session_state:
        st.session_state["count"] = 0

    if st.button("Session State +1"):
        st.session_state["count"] += 1

    st.write("session_state count:", st.session_state["count"])

    if st.button("Session State 초기화"):
        st.session_state["count"] = 0
        st.rerun()

    st.caption("같은 브라우저 세션 안에서는 값이 계속 유지됩니다.")

st.divider()

st.write(
    "정리: Streamlit 앱은 사용자 입력이 발생할 때마다 다시 실행되므로, "
    "화면 조작 후에도 값을 유지하려면 `st.session_state`를 사용합니다."
)
