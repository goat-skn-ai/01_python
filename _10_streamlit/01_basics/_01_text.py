import streamlit as st

# streamlit 실행 명령어: streamlit run [파일명].py

# title: 제목
st.title("🎃Hello Streamlit🎃")

st.header("Text")
st.subheader(":blue[write]", divider="blue")

# write: 텍스트 출력
# st.write()가 문자열뿐 아니라 표, 리스트, 차트 등 입력 타입에 따라 다르게 출력된다
st.write("streamlit은 **markdown**을 지원합니다. :smile:")
st.markdown("`write` 또는 `markdown` 메서드를 사용하세요.")
st.html("<h3>심지어 HTML도 지원합니다.</h3>")

st.subheader(":red[magic]", divider="red")
st.write('Streamlit은 변수나 리터럴 값이 한 줄에 따로 있는 것을 발견하면 자동으로 화면에 값을 기록합니다.')

100
"magic text"
lst = [10,20,30]
lst

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

st.subheader(":green[badge]", divider="green")

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)