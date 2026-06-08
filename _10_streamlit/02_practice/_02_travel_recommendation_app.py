import streamlit as st


# 실행 명령어:
# streamlit run _02_travel_recommendation_app.py

# 예제 목표:
# - text_input(), checkbox(), selectbox()를 사용해 입력을 받는다.
# - 입력 결과에 따라 success(), warning(), info() 메시지를 다르게 출력한다.
# - 조건문으로 사용자 입력에 따른 화면 변화를 만든다.

st.title("여행지 추천 입력 앱")

st.write("여행지와 여행 스타일을 입력하면 간단한 추천 메시지를 출력합니다.")

# 사용자가 가고 싶은 여행지를 직접 입력한다.
destination = st.text_input(
    label="가고 싶은 여행지",
    placeholder="예: 제주도, 부산, 도쿄"
)

# checkbox()는 True 또는 False 값을 반환한다.
with_companion = st.checkbox("동행자가 있습니다.")

# selectbox()는 정해진 선택지 중 하나를 선택하게 할 때 사용한다.
travel_style = st.selectbox(
    label="선호하는 여행 스타일",
    options=[
        "휴식",
        "맛집 탐방",
        "자연 경관",
        "액티비티",
        "문화/역사"
    ]
)

# 입력된 여행지가 없으면 추천 메시지를 만들 수 없으므로 경고 메시지를 출력한다.
if not destination:
    st.warning("먼저 가고 싶은 여행지를 입력해 주세요.")
else:
    st.success(f"{destination} 여행 계획을 만들어 볼 수 있습니다.")

    if with_companion:
        st.info(f"동행자와 함께라면 {travel_style} 중심의 일정을 함께 조율해 보세요.")
    else:
        st.info(f"혼자 여행이라면 {travel_style} 일정을 여유 있게 구성해 보세요.")

    # 여행 스타일별로 조금 다른 추천 문장을 출력한다.
    if travel_style == "휴식":
        st.write("추천: 숙소 위치와 이동 시간을 줄이는 일정이 좋습니다.")
    elif travel_style == "맛집 탐방":
        st.write("추천: 식사 시간대별 후보 맛집을 미리 정리해 보세요.")
    elif travel_style == "자연 경관":
        st.write("추천: 날씨와 일몰 시간을 함께 확인하면 좋습니다.")
    elif travel_style == "액티비티":
        st.write("추천: 예약 가능 여부와 준비물을 먼저 확인하세요.")
    else:
        st.write("추천: 박물관, 유적지, 전시 공간을 중심으로 동선을 잡아 보세요.")
