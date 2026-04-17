# a=int(input('나이를 숫자로 입력해 주세요 : '))
# if(a>=20):
#     print("성인입니다.")
# elif(a<=0):
#     print('아직 태어나지 않으셨군요?')
# elif(0<a<=12):
#     print('아이입니다.')
# else:
#     print('청소년입니다.')
# try:
#     num=int(input('숫자 홀수 짝수 판별기 : '))
#     if(num%2==1):
#         print(f'{num}은(는) 홀수입니다.')
#     else: print(f'{num}은(는) 짝수입니다.')
# except:
#     print('입력한 값은 숫자가 아닙니다.')

# try:
#     num=int(input('점수를 숫자로 입력하세요 : '))
#     if(100>=num>=90):
#         print(f'{num}점은 A입니다.')
#     elif(80<=num<90):
#         print(f'{num}점은 B입니다.')
#     elif(70<=num<80):
#         print(f'{num}점은 C입니다.') 
#     elif(60<=num<70):
#         print(f'{num}점은 D입니다.')
#     elif(0<=num<60):
#         print(f'{num}점은 F입니다.')
#     else:
#         print('점수는 100점을 넘거나 0점아래로 내려갈 수 없습니다.')
# except:
#     print('입력한 값은 숫자가 아닙니다.')
# i=0
# while(i<=100):
#     if(i<30):
#         print(i)
#         i+=2
#     else : 
#         print(i)
#         i+=10
# num=0
# while num<10:
#     num=num+1
#     print(f"양이 {num}마리 나갔습니다.")
#     if num==10:
#         print("양이 다 나갔습니다.")

# num=0
# for i in range(1,1001):
#     if i%3==0:
#         num+=i
# print(num)

# A=[20,55,67,82,45,33,90,87,100,25]
# avg=0
# B=[]
# for a in A:
#     if a>=50:
#         B.append(a)
# avg=sum(B)/len(B)
# print(avg)

# for i in range(2,10):
#     for j in range(1,10):
#         print('{}*{}={:2d}'.format(i,j,i*j),end=' ')
#     print()

# import numpy as np
# print(np.arange(10,0,-0.7))
# avg=0
# sum=0
# A=[70,60,55,75,95,90,80,80,85,100]
# for i in A:
#     sum+=i
# avg=sum/len(A)
# print(avg)
# mixed = [42, "hello", 3.14, True, [1, 2, 3], "python", 7, False, 2.71, "AI"]
# num_total = 0
# words = []
# bool_count = 0
# for i in mixed:
#   if type(i)==bool:
#     bool_count+=1
#   elif type(i)==int or type(i)==float:
#     num_total+=i
#   elif type(i)==str:
#     words.append(i)
#   else : print(f"기타 : {type(i)}")
# print(f"숫자 합계: {num_total}")
# print(f"문자열 목록: {words}")
# print(f"bool 개수: {bool_count}")

# sentence = "The quick brown fox jumps over the lazy elephant"

# word_dict = {}

# for i in sentence.split():
#     if len(i)>=4:
#         word_dict.update({i:len(i)})
#     else: print(i[::-1])
# print(word_dict)

# print(f"가장 긴 단어는 {(max(word_dict.keys()))} ({max(word_dict.values())}글자)")

# cart = {"사과": 1200, "바나나": 800, "포도": 2500, "수박": 15000, "딸기": 3000}

# expensive = set()
# cheap = set()
# total = 0

# # 여기에 코드를 작성하세요
# for i in cart.items():
#   if cart[i[1]]>5000:
#     expensive.add(i)
#     print(f"{i.keys}: {i.values} -> {i.values*0.8}(20% 할인)")
#   else : 
#     print(f"{i.keys}: {i.values} -> {i.values*0.9}(10% 할인)")
#     cheap.add(i)
# # 총 결제금액, 고가/저가 집합 출력
# print(expensive,cheap)
numbers = [3, 8, 15, 12, 7, 20, 5, 32, 18, 41, 6, 28, 44, 11, 36]

evens = []

# (1) for + continue: 홀수 건너뛰고 짝수만 evens에 추가
# 여기에 코드를 작성하세요
for i in numbers:
  if(i%2==1):
    continue
  else: evens.append(i)
evens1=[]
for j in evens:
  if j>=30:
    print(f"처음으로 30초과 : 인덱스 {len(evens1)} 값{j}")
    break
  evens1.append(j)
print(f"짝수 리스트: {evens}")
print()