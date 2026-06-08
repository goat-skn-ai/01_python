import streamlit as st
import pandas as pd


# 판다스란?
# pandas는 데이터 분석과 조작을 위해 설계된 파이썬 라이브러리로,
# 특히 구조화된 데이터(예: 테이블 형태의 데이터) 처리가 강력하다.
# pandas는 데이터프레임(DataFrame)이라는 구조를 중심으로 빠르고 직관적인 데이터 처리 및 분석을 지원한다.

st.title("😊Data😊")

st.header("pandas' DataFrame")

# 정형데이터 (행/열)
# - dict전달 (컬럼명:컬럼값)
students_df = pd.DataFrame({
    'Name': ['홍길동', '신사임당', '이순신'],
    'Age': [33, 48, 53],
    'Score': [90, 86, 79]
})
st.dataframe(students_df)

sample_df = pd.read_csv('data/annual-enterprise-survey-2023.csv')
st.dataframe(sample_df)



st.html("<hr>")
st.header("Example 2")

# 판매 데이터 생성
data = {
    "Product": ["A", "B", "C", "D"],
    "Sales": [500, 300, 400, 600],
    "Growth (%)": [10, -5, 15, 7]
}
df = pd.DataFrame(data)

# DataFrame을 시각적으로 강조하여 출력
st.dataframe(df.style.highlight_max(subset="Sales", color="lightgreen")
             .highlight_min(subset="Growth (%)", color="pink"))

# 열 설정을 추가한 DataFrame 표시
st.dataframe(df, column_config={
    "Sales": st.column_config.NumberColumn("Total Sales", format="%d units"),
    "Growth (%)": st.column_config.NumberColumn("Growth Percentage", format="%.1f%%")
}, width="stretch")