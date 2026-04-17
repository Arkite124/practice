# 자료형 - list,tuple,index,%s,%c,%d 등 
# korean=80
# english=75
# mathamatics=55

# hap=korean+english+mathamatics
# average=hap/3
# print('평균은', average,'점입니다.')
# print('홀수 판별기입니다. 숫자만 입력해 주세요.')
# user_input=input()
# if(int(user_input)%2==1): 
#     print('짝수 입니다')
# else:
#     print('홀수 입니다.')
# na='친구가 \"햇님이 좋아\" 라고 말했다'
# print(na)
# txt="""
# 큰 따옴표"" 와\n 작은 따옴표 ''를 \n 모두 포함한 문장
# """
# print(txt)

# print("I eat %s apples" %'five')
# number=10
# day='three'
# print("I eat %d apples in %s days"%(number,day))
# a=444.56767677
# print("%20.3f" %a)

# a="https://daum.net"
# a=a.replace("https://","")
# a=a[:a.index(".")]
# password=a[:3]+str(len(a))+str(a.count("d"))+"@"

# print(password) 
# lists=[100,200,400]
# fruits=["apple","orange","banana"]
# mixed_list=lists+fruits
# print(mixed_list)
# even_list=[2,4,6,8,10]
# even_list=list(range(2,11,2))
# print(even_list)
# # nations=['korea','china','nepal','India']
# # print(nations)
# Strings='XYZ'
# print(list(Strings))
# n_list=list(range(0,15))
# s_list1=list(n_list[:5])
# s_list2=list(n_list[5:11])
# s_list3=list(n_list[11:])
# s_list4=list(n_list[2:11:2])
# s_list5=list(n_list[-5:-10:-1])
# s_list6=list(n_list[-5:-14:-2])
# print(s_list6)
# n_list=list(range(11,67,11))
# print(n_list)
# del n_list[3]
# print(n_list)
# print(n_list.pop())
# print(n_list)

# t_fruits=('orange','banana','water melon')
# print(type(t_fruits))
# # list로 변환
# t_list=list(t_fruits)
# print(type(t_list))
# # 다시 tuple로 변환
# f_fruits=(tuple(t_list))
# print(type(f_fruits))
# 튜플에 원소 추가 tuple -> list -> append -> tuple
t=1,2,3
print(t)
t=list(t)
t.append(4)
t=tuple(t)
print(t)