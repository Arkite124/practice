# f=open("./day4/사람의 파일.txt",'r')
# x=f.read()
# print(x)
# f.close()
# f=open("./day4/사람의 파일.txt",'w')
# for i in range(1,11):
#     data="%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
f=open("./day4/사람의 파일.txt",'a')
for i in range(11,21):
    data="%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
with open("./day4/사람의 파일.txt",'r') as file:
    content=list()
    # while True:
    #     sentence=file.readline()
    #     if sentence:
    #         content.append(sentence)
    #     else : break
    for f in file:
        content.append(f.split("\n")[0])
    print(content)