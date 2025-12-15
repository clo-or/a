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


st.image("data/naver_news_network.png", use_container_width=True)

# :blue[위젯]

### : orange [다운로드 버튼: st.download_button()]
with open("data/naver_news_network.png", "rb") as file:
    st.download_button(
        label='이미지 파일 다운로드',  # 버튼 라벨
        data="data/naver_news_network.png",                    # 다운로드할 파일 경로
        file_name='network.png',        # 다운로드 파일명
        mime='image/png'              # 파일 형식
    )

st.image("data/naver_news_circle_network.png", use_container_width=True)

# :blue[위젯]

### : orange [다운로드 버튼: st.download_button()]
with open("data/naver_news_circle_network.png", "rb") as file:
    st.download_button(
        label='이미지 파일 다운로드',  # 버튼 라벨
        data="data/naver_news_circle_network.png",                    # 다운로드할 파일 경로
        file_name='network_circle.png',        # 다운로드 파일명
        mime='image/png'              # 파일 형식
    )

st.image("data/wordcloud.png", use_container_width=True)

# :blue[위젯]

### : orange [다운로드 버튼: st.download_button()]
with open("data/wordcloud.png", "rb") as file:
    st.download_button(
        label='이미지 파일 다운로드',  # 버튼 라벨
        data="data/wordcloud.png",                    # 다운로드할 파일 경로
        file_name='cloud.png',        # 다운로드 파일명
        mime='image/png'              # 파일 형식
    )

st.image("data/wordcloud.png", use_container_width=True)

# :blue[위젯]

### : orange [다운로드 버튼: st.download_button()]
with open("data/wordcloud_square.png", "rb") as file:
    st.download_button(
        label='이미지 파일 다운로드',  # 버튼 라벨
        data="data/wordcloud_square.png",                    # 다운로드할 파일 경로
        file_name='cloud_square.png',        # 다운로드 파일명
        mime='image/png'              # 파일 형식
    )

st.header('1. Button')
if st.button('Say hello'):
    st.write('HELL_O')

