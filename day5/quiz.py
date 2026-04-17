# # 1번
# class Book:
#     title=""
#     author=""
#     price=""
# b1=Book()
# b1.title="파이썬 기초"
# b1.author="홍길동"
# b1.price=25000
# print(b1.title,b1.author,b1.price)
# # 2번
# class Timer:
#     def __init__(self):
#         self.count=0
#     def tick(self,n):
#         self.count+=n
#         return self.count
# t1=Timer()
# t2=Timer()
# print(t1.tick(5),t1.tick(3),t1.tick(10),t1.tick(2))
# # 3번
# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     def get_info(self):
#         print(f"이름: {self.name}, 학점: {self.grade}")
#         return self.name,self.grade
# s1=Student("김민준",4.3)
# s1.get_info()
# # 4번
# class ScoreBoard:
#     total=0
#     def __init__(self,score):
#         self.score=score
#         ScoreBoard.total+=score
# s1=ScoreBoard(80)
# s2=ScoreBoard(90)
# s3=ScoreBoard(70)
# print(ScoreBoard.total,s1.score)
# # 5번
# import numpy as np
# a = np.array([3, 6, 9, 12, 15])
# print(a[2],a[-1],a[1:4])
# # 6번
# import numpy as np
# z=np.zeros(4)
# o=np.ones(3)
# r=np.arange(2,10,2)
# print(z)
# print(o)
# print(r)
# # 7번
# import numpy as np
# a=np.arange(1,7)
# b=a.reshape(2,3)
# print(b,b.shape)
# # 8번
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def get_info(self):
#         return print(f"상품명: {self.name},상품 정가: {self.price}")
#     def sale_price(self,rate):
#         try:
#             rate=int(rate)
#             discount_price=self.price*(1-rate/100)
#             return print(f"할인가 : {discount_price}")
#         except Exception:print("할인율은 숫자여야 합니다.")
# p1=Product("노트북",1500000)
# p1.get_info()
# p1.sale_price("10")
# # 9번
# import numpy as np
# mat=np.arange(1,10)
# mat=mat.reshape(3,3)
# print(mat)
# print(mat[1][2])
# print(mat+10)
# # 10번
# import numpy as np
# class ScoreManager:
#     def __init__(self,scores):
#         self.data=np.array(scores)
#     def get_total(self):
#         print(f'합계 : {np.sum(self.data)}')
#     def get_average(self):
#         print(f'평균 : {np.sum(self.data)/len(self.data)}')
#     def get_above(self,cutoff):
#         print(f"80점 초과 {np.array([i for i in self.data if i>cutoff])}")
# scores = [72, 88, 95, 61, 84, 77] 
# ScoreManager(scores).get_total()
# ScoreManager(scores).get_average()
# ScoreManager(scores).get_above(80)

