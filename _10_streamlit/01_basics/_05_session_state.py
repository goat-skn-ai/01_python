import streamlit as st

st.title("Session State")

st.header("Counter")

# - Streamlit은 버튼 클릭 같은 사용자 상호작용이 발생하면 스크립트를 위에서 아래로 다시 실행한다.
# - 그래서 일반 변수는 매번 다시 초기화되고, session_state는 같은 사용자 세션 안에서 값을 유지한다.
count: int = 0 # 초기화

if st.button('버튼'):
    count += 1

st.write(f"누른 횟수 : {count}")

st.header("Session State의 Counter")
# session_state: 서버 컴퓨터의 메모리 영역에 사용자별 객체공간
if "count" not in st.session_state:
    st.session_state["count"] = 0 # 초기화
    print('session_state["count"]가 초기화 되었습니다.')

if st.button("Button"):
    st.session_state["count"] += 1

st.write(f'누른 횟수: {st.session_state["count"]}')

if st.button("Reset"):
    st.session_state["count"] = 0
    st.rerun()