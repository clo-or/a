import streamlit as st

st.set_page_config(  # 페이지 설정
    page_title="케이팝 데몬 헌터스 팬덤 형성 요인 분석",  # 페이지 Tab의 타이틀
    page_icon="",  # 페이지 Tab의 아이콘
    layout="wide",  # 페이지 레이아웃: centered, wide
    # 사이드바 초기 상태 : auto, collapsed, expanded
    initial_sidebar_state="expanded",
    # 페이지 오른쪽 상부의 메뉴에 추가할 메뉴 항목: Get help, Report a bug, About
    menu_items={
        'Get help': "https://docs.streamlit.io",  # URL만
        'Report a bug': "https://streamlit.io",  # URL만
        'About': "## C321050 이승아"
    }
)
st.set_page_config(
    page_title="Streamlit",
    layout="wide",
    initial_sidebar_state="expanded"
)


# 타이틀 텍스트 출력
st.title("C321050 이승아 데이터 시각화 3차 시험")


st.header('워드클라우드 이미지')

st.subheader('워드클라우드 이미지이다.')
st.text('이를 통해 한국 관람, 음식 등 한국의 문화와 영화 내 아이돌 그룹 (헌트릭스), 빌보드 (노래) 등 잘 만들어진 영화 내 노래가 핵심 요인임을 볼 수 있다.')
if st.button('워드클라우드 이미지 기본'):
    st.image("data/wordcloud_square.png", use_container_width=True)

st.subheader('워드클라우드 도형 이미지이다.')
st.caption('데이터 분석 관점에서 필요하진 않으나 시각화의 미적요소를 위해 완성하였다.')
if st.button('워드클라우드 이미지 하트'):
    st.image("data/wordcloud.png", use_container_width=True)

primary_button = st.button('케데헌 헌트릭스 golden 뮤직비디오 보기', type='primary')
if primary_button:
    st.video("https://www.youtube.com/watch?v=yebNIHKAC4A&list=RDyebNIHKAC4A&start_radio=1")  # YouTube 링크

st.header('네트워크 이미지')

st.subheader('기본 네트워크 이미지이다.')
st.text('음식(떡볶이, 김밥, 라면)등이 대체적으로 이어져있고, 라이프스타일, 전통, 호랑이, 관광등이 형성되어있는 것을 보아, 대표적인 한국 라이프스타일과 문화를 볼 수 있는 영화가 팬덤 형성의 핵심 요인이 되었다는 것을 확인할 수 있다.')
if st.button('네트워크 시각화 이미지'):
    st.image("data/naver_news_network.png", use_container_width=True)

st.subheader('네트워크 원형 이미지이다.')
st.text('위에서 언급했던 것과 같이 음식, 전통 등 한국의 라이프 스타일을 볼 수 있는 영화이기 때문에 팬덤이 형성되었다는 것을 확인할 수 있다.')

if st.button('네트워크 시각화 이미지 원형'):
    st.image("data/naver_news_circle_network.png", use_container_width=True)







