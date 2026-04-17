# # 1번
# calc=lambda a,b:a*b 
# print(calc(6,8))
# print(calc(3,7))
# # 2번
# scores=[85,42,91,67,55,78]
# result=lambda x:x>70
# print(list(filter(result,scores)))
# # 3번
# nums=[2,3,4,5]
# result=lambda x:x*3
# print(list(map(result,nums)))
# # 4번
# print([i*2 for i in range(1,6)])
# # 5번
# product = "노트북"
# price = 1200000
# qty = 2
# print("상품:{product}, 가격:{price}원, 수량: {qty}개".format(product=product,price=price,qty=qty))
# # 6번
# a,b=(map(int,input("공백으로 두 정수를 써 주세요.").split()))
# print(f"합 : {a+b}")
# print(f"곱 : {a*b}")
# # 7번
# import math
# print(math.sqrt(144))
# print(math.pow(2,10))
# # 8번
# print([i**2 for i in range(1,21) if i%3==0])
# # 9번
# try:
#     name,price=input("상품명,가격 순서대로 입력해 주세요.").split()
#     if price.isdigit():
#         b_int=int(price)
#         a_int=name
#     elif name.isdigit():
#         b_int=int(name)
#         a_int=price
#     print("상품명: {a}, 정가: {b:,} 할인가(10%):{c:.2f}".format(a=a_int,b=b_int,c=b_int*0.9))
# except:print("가격은 정수여야 합니다.")
# # 10번
# import math
# from functools import reduce
# data=list(map(int,input("공백으로 여러 개의 정수를 써 주세요.").split()))
# evens=[i for i in data if i%2==0]
# total=reduce(lambda x,y:x+y,evens) 
# print(f"짝수 목록 {evens}")
# print(f'합계 : {total}')
# print("제곱근 : {:.3f}".format(math.sqrt(total)))
