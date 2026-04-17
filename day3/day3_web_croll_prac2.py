from bs4 import BeautifulSoup

html_doc = """
<p class="price_color"> £51.77 </p>
<h1> 상품 상세 정보 <br> 새로운 기능! </h1>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

# 가격 추출 및 정제
price_tag = soup.find('p', class_='price_color')
price_text = price_tag.get_text(strip=True) # "£51.77"
clean_price = float(price_text.replace('£', '')) # 51.77

# 제» 텍스트 추출 및 정제
# .text는 자식 태그의 텍스트도 포함 (줄바꿈 포함)
title_raw = soup.find('h1').text
# .get_text(strip=True)는 o든 공백 제거 후 텍스트만 반환
title_clean = soup.find('h1').get_text(' ', strip=True) 
# "상품 상세 정보 새로운 기능!"
print(f"원시 가격: {price_text}")
print(f"정제된 가격: {clean_price}")
print(f"원시 제목: '{title_raw}'")
print(f"정제된 제목: '{title_clean}'")