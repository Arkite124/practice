import csv
import pprint

# with open("movies.csv") as file:
#     reader=csv.reader(file)
#     movies=list(reader)

# pprint.pprint(movies)

# txt=input("저장할 내용을 입력하세요.")
# with open("test2.txt",'a',encoding='utf-8') as file:
#     file.write(txt+"\n")

# file= open("test.txt",'r')
# content=file.read()
# file.close()
# content2=content.replace("java","python")
# file2=open("test.txt",'w')
# file2.write(content2)
# print(content2)
# file2.close()

file=open("sample.txt",'r',encoding='utf-8')
numbers=file.readlines()
numbers2=[x.replace("\n","") for x in numbers]
numbers3=[int(x) for x in numbers2]
sum_num=sum(numbers3)
avg_num=sum_num/(len(numbers3))
file.close()
with open("result.txt",'w',encoding='utf-8') as file2:
    file2.write(f"평균값은 {avg_num} 입니다.")