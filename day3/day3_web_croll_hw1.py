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
books=scope_data.find_all('article')
book_star_rating=scope_data.find_all('p',class_="star-rating One")
# print(books)
rating_map={"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
book_data=[]
star_rating_score=0
for book in books:
    title=book.h3.a['title']
    star_rating_score=book.find('p',class_="star-rating")["class"]
    rating=rating_map[star_rating_score]
    book_data.append({"title":title,"Star-rating":star_rating_score})
print(book_data)
