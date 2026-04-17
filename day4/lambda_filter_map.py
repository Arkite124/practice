# myList=[lambda a,b : a+b,lambda a,b : a*b]
# print(myList[0](2,4))
# lambda -> lambda 변수 : return값 
# 간결한 과정 정의 및 결과값 출력에 사용
# # function
# def sub1(a,b):
#     return print(f"{a}-{b}={a-b}")
# sub1(200,100)
# # lambda
# sub2=lambda a,b : print(f"{a}-{b}={a-b}")
# sub2(200,100)
# # 결과값이 같음
n_list=list(range(1,11))
print(n_list)
even_list=[]
# for x in n_list:
#     if x%2==0:
#         even_list.append(x)
even_list=list(filter(lambda x:x%2==0, n_list))
print("even_list :",even_list)
odd_list=list(filter(lambda x:x%2==1, n_list))
print("odd_list :",odd_list)
