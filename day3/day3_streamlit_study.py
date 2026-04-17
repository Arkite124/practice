import streamlit as st
import pandas as pd
import json
from bs4 import BeautifulSoup
import requests

st.title("나의 웹 사이트")
st.header("메인 콘텐츠 섹션")
col1, col2= st.columns({1,2})
with col1:
    st.subheader("사이드 패널")
    st.write("왼쪽")
with col2:
    st.subheader("주요 정보")
    st.write("오른쪽")
# 'counter' 변수 초기화
if 'count' not in st.session_state:
    st.session_state.count = 0

st.write("현재 카운트:", st.session_state.count)

def increment_num():
    st.session_state.count+=1
    if st.session_state.count>10:
         st.session_state.count=0

st.button("카운트 증가",on_click=increment_num)

# 숫자 입력
age = st.number_input("나이를 입력하세요", min_value=0,
max_value=120)
st.write(f"나이: {age}")

# 슬라이더
level = st.slider("난이도 선택", 1, 10, 5)
st.write(f"선택된 난이도: {level}")

# 드롭다운 (단일 선택)
fruit = st.selectbox("좋아하는 과일은?", ("사과", "바나나", "오렌지"))
st.write(f"선택된 과일: {fruit}")

# 다중 선택
colors = st.multiselect("좋아하는 색상", ["빨강", "파랑", "초록",
"노랑"])
st.write(f"선택된 색상: {', '.join(colors)}")

# 체크박스
agree = st.checkbox("동의합니다")
if agree:
    st.write("동의 완료!")

# 날짜 선택
import datetime
today = st.date_input("오늘 날짜", datetime.date.today())
st.write(f"선택된 날짜: {today}")

# --- 데이터 수집 ---
url = "http://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').get_text(strip=True)
    clean_price = float(price.replace('Â£', '')) # 51.77
    data.append({'title': title, 'price': f"₩ {int(clean_price*1995)}"})

# --- 웹 화면 ---
st.title('책 가격 비교')
keyword = st.text_input('책 제목 검색')

df = pd.DataFrame(data)
if keyword:
    df = df[df['title'].str.contains(keyword, case=False)]

st.dataframe(df)

