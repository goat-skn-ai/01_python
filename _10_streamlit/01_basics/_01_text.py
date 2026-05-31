import streamlit as st

# streamlit 실행 명령어: streamlit run [파일명].py

# title: 제목
st.title("🎃Hello Streamlit🎃")

# write: 텍스트 출력
st.write("streamlit은 **markdown**을 지원합니다. :smile:")
st.markdown("`write` 또는 `markdown` 메서드를 사용하세요.")
st.html("<h3>심지어 HTML도 지원합니다.</h3>")

# latex: 수학 식
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# columns(n): 컬럼 분할
col1, col2, col3 = st.columns(3)

# metric(label, value, delta): 수치 메트릭 표시(제목, 값, 변화량)
col1.metric(label="달러USD", value="1,228 원", delta="-12.00 원")
col2.metric(label="일본JPY(100엔)", value="958.63 원", delta="-7.44 원")
col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")