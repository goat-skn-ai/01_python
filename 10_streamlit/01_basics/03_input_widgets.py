import streamlit as st

st.title('☑️Input Widgets☑️')

st.header('Button')

clicked = st.button('Click Me')
print(f'clicked = {clicked}')

if clicked:
    st.write('버튼을 누르셨군요~ 🎃')
else:
    st.write('제발~ 제바아아아알ㄹㄹㄹㄹㄹ~')

st.header('Text Input')
input = st.text_input(
    label='가고 싶은 여행지가 있으세요?',
    placeholder='여행지를 입력하세요.'
)
print(f'input = {input}')
if input:
    st.write(f'당신은 :blue[{input}]에 가고 싶으시군요~')

st.header('Checkbox')
agree = st.checkbox("I agree")
print(f'agree = {agree}')
if agree:
    st.write("Great!")

st.header('SelectBox')
# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ',
     'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP',
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
     '모름'),
    index=7
)
if mbti:
    st.write(f'선택한 MBTI는 :red[{mbti}]입니다.')
