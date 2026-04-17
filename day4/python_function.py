import datetime as dt
import random
# x=dt.datetime.now()
# date_x=list(str(x).split())
# date_x_list=list(date_x[0].split("-"))
# print(date_x_list)
# x_str="I like {0} and {1}".format("python","java")
# print(x_str)
# for i in range(2,15,2):
#     print('{0:3d},{1:4d},{2:5d}'.format(i,i**2,i**3))
# lat='35.17N'
# long='129.07E'
# print('위도 : {lat}, 경도 : {long}'.format(lat=lat,long=long))
# print(f"위도 : {lat}, 경도 : {long}")
numbers=input('숫자를 콤마로 구분해서 입력하세요.')
list_a=numbers.split(",")
num_list=[int(x) for x in list_a]
sum_num=sum(num_list)
print(f"총 합은 {sum_num}입니다.")