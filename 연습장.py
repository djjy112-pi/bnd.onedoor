import streamlit as st

st.title("🎈 My new app")
st.write(
    "반갑습니다. 저는 1-9 이지윤입니다."
)
st.success( "반갑습니다. 저는 1-9 이지윤입니다.")
st.info("반갑습니다. 저는 1-9 이지윤입니다.")
st.image("https://www.google.com/imgres?q=%ED%95%9C%ED%83%9C%EC%82%B0&imgurl=https%3A%2F%2Fmedia.bunjang.co.kr%2Fproduct%2F348232582_1_1754007424_w360.jpg&imgrefurl=https%3A%2F%2Fm.bunjang.co.kr%2Fproducts%2F348232582&docid=zrHq0DEAHdMJsM&tbnid=MnEc0PncNj_gQM&vet=12ahUKEwiy_9GzyoKQAxXgdfUHHVBBGxUQM3oECCAQAA..i&w=360&h=360&hcb=2&ved=2ahUKEwiy_9GzyoKQAxXgdfUHHVBBGxUQM3oECCAQAA")
# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")
# 페이지 구조용 제목 출력
st.title("저녁메뉴추천")
st.header("좋은 저녁 되세요")
st.subheader("맘스터치,콜라,감튀")
# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성
    # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
    # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")
    # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)
# st.empty(): 동적으로 내용을 업데이트할 수 있는 빈 컨테이너입니다
placeholder = st.empty()
placeholder.write("잠시 후 이 자리에 내용이 바뀝니다.")

import time
time.sleep(2)
placeholder.write("⏳ 내용이 업데이트되었습니다!")
# st.container(): 특정 영역 안에 여러 컴포넌트를 묶어 배치합니다
with st.container():
    st.subheader("📦 이 영역은 하나의 컨테이너입니다.")
    st.write("여기에 다양한 요소를 넣을 수 있습니다.")
    st.line_chart({"data": [1, 5, 2, 6]})
    # 버튼 클릭 여부에 따라 실행
if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")
    # 한 줄 텍스트 입력
name = st.text_input("이름을 입력하세요")
st.write("입력된 이름:", name)

# 여러 줄 텍스트 입력
feedback = st.text_area("의견을 입력하세요")
st.write("입력된 의견:", feedback)
# 정수 혹은 실수 입력


age = st.number_input("나이를 입력해주세요")

## 입력
st.write(2025-age)
st.write(f"{2025-age}년에 태어나셨군요")


# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)


# 날짜 입력
date = st.date_input("날짜를 선택하세요")
st.write("선택한 날짜:", date)

# 시간 입력
time = st.time_input("시간을 선택하세요")
st.write("선택한 시간:", time)

# 카메라로 사진 촬영
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)
    