import requests
from bs4 import BeautifulSoup
def code_name(a):
    if a==200:
        return "정상"
    if a==400:
        return "잘못된 요청"
    if a==403:
        return "권한 차단"
    if a==404:
        return "잘못된 페이지"
    return "그 외 서버오류"
url="http://books.toscrape.com/"
data=requests.get(url)
print("요청 응답 상태 :","\""+code_name(data.status_code)+"\"")
scope_data=BeautifulSoup(data.text,"html.parser")
books=scope_data.find_all('article',class_="product_pod")
# print(books)
book_data=[]
for book in books:
    title=book.h3.a['title']
    price=book.find('p',class_="price_color").text
    book_data.append({"title":title,"price":price})
print(book_data[5:8])
