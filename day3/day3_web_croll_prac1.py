from bs4 import BeautifulSoup
html_doc = """
<div id="product-123" class="item featured" data-stock="10">
<a href="/detail/book-title-1">Book Title</a>
<img src="/images/book1.jpg" alt="Book Cover">
</div>
"""
soup=BeautifulSoup(html_doc,"html.parser")
product_div=soup.find("div")
link=soup.find('a')['href']
print("link : "+link)
link2=soup.a['href']
print("link2 : "+link2)
image = soup.find('img')
product_id=product_div['id']
print("product_id : "+ product_id)
item_classes = product_div['class'] # ["item", "featured"]
stock = product_div.get('data-stock') # "10"
# .get()으로 안전하게 접근 (없는 속성은 None 반환)
missing_attr = product_div.get('data-price', 'N/A') # "N/A"
img_alt = image.get('alt') # "Book Cover"
print(f"ID: {product_id}, Class: {item_classes}")
print(f"Stock: {stock}, Missing: {missing_attr}, Alt: {img_alt}")