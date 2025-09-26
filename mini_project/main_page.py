import streamlit as st

# 꼭 맨 위에!
st.set_page_config(layout="wide")

# --- 배경 이미지 CSS만 적용 ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeux9w24PK9nwHfnvIzxBYsi6fLaefmu6JpA&s');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목 및 선택박스
st.markdown(
    "<h1 style='text-align: center;'>옵션 선택</h1>",
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns(3)

# ✅ 선택박스 (드롭다운)
with col3:
    selected = st.selectbox("옵션을 선택하세요:", ["옵션 1", "옵션 2", "옵션 3"])

    self_checkin = st.checkbox("셀프 체크인")
    wifi = st.checkbox("WIFI")
    parking = st.checkbox("주차 가능")

    selected_options = []
    if self_checkin:
        selected_options.append("셀프 체크인")
    if wifi:
        selected_options.append("WIFI")
    if parking:
        selected_options.append("주차 가능")

    if selected_options:
        st.write("선택한 옵션:", ", ".join(selected_options))
    else:
        st.write("아직 선택한 옵션이 없습니다.")

    st.markdown(
    """
    <style>
    /* 체크박스 라벨 텍스트 스타일 */
    .streamlit-expanderHeader label,  /* 혹시 expander 안에 있다면 */
    div[data-testid="checkbox"] label {
        font-weight: 700 !important;       /* 두껍게 */
        color: #0066CC !important;          /* 파란색 텍스트 */
        background-color: #F0F8FF !important;  /* 연한 하늘색 배경 */
        padding: 5px 10px;
        border-radius: 5px;
        display: inline-block;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    # 에어비앤비 사이트 링크

st.write('에어비앤비 바로가기 >> https://www.airbnb.co.kr/')


"""
neighbourhood_cleansed: 아다치 구, 어떤 구, 어떤 구 지역 선택
room_type: apt, hotel, private, shared 선택
accommodates는 최대 수용 인원. 2명 선택하면 accommodates는 2명 이상으로 되는 게 맞긴한데
bathrooms: 화장실 개수. 누가 치나 이런 걸
    -> 만약 선택 안 하면 기본 1개.
bedrooms: 침실 개수. 직접 입력하는 창 생성? (0~25)
beds: 침대 개수. 직접 입력하는 창 생성?
review_scores_rating: 별점 몇 점 이상으로 ... -> 피쳐값으론 (5-(입력값))/2
amnt: 셀프 체크인, 주방유무, 헤어드라이기, 프리파킹, 와이파이, 에어컨


neighbourhood_cleansed: 
! room_type: 네 개 셀렉트 박스
! accommodates: 1~16 셀렉트 박스

bathrooms: 
review_scores_rating: 범위를 0~3, 3~4, 4~5로 나누고 피쳐로는 1.5, 3.5, 4.5 넘기기?
amnt: 주요 편의 시설만 버튼 생성. 그럼 남은 피쳐는...?
"""