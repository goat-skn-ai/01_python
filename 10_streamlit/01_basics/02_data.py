import streamlit as st
import pandas as pd

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