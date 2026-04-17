# person={'이름':'홍길동','몸무게':90,'키':185}
# # print(person['주소'])
# # 없는 key값이라 오류
# add_person={'주소':'서울'}
# add_person2={'일생':'불쌍'}
# person.update(add_person)
# print(person['주소'])
# # person의 주소라는 key값이 붙어 value가 출력
# del person['키']
# print(person)
# # 키라는 key값이 삭제 됨 -> json구조와 유사 변환
# # print(type(person)) # dict
# person['직업']='도둑의 왕'
# person.update(add_person2)
# print(person)
# person.clear()
# # dict 항목 삭제
# person.update(add_person)
# person.update(add_person2)
# print(person)
# dict_prac={'name':'홍길동','birth':1128,'age':30}
# dict_prac.pop('age')
# print(dict_prac)
# a={'A':90,'B':80,'C':70}
# value_a=list(a.values())
# print('min :',min(value_a))
# print(list(a.items()))

# fruits_dic={'apple':6000,'melon':3000,'banana':5000,'orange':4000}
# print(list(fruits_dic.keys()))
# print(list(fruits_dic.values()))
# print(len(fruits_dic))
# if 'apple' in fruits_dic:
#     print('apple is in fruits_dic')
# else : print('mango is not in fruits_dic')

# s=set(['a','b'])
# print(type(s))
# a=[1,1,1,2,2,2,2,3,3,3,3,3,4,4,5,5,5,5,5]
# print(a)
# # 중복 제거
# a=set(a)
# a=list(a)
# # 집합 후에 다시 리스트 변환
# print(a)
# # 집합의 연산 
# s1=set(['a','b','c','d','e'])
# s2=set(['c','d','e','f'])
# print(s1-s2)
a=[1,2,3]
a+[4,5]
print(id(a))
a.extend([6,7])
print(id(a))
a=[1,[2,3],4]
import copy
b=copy.deepcopy(a)
a[1][0]=5
print(a,b)