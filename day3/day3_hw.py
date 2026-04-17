# # 1번
# def print_line():
#     print("=============================")
# print_line()
# # 2 번
# def get_sum(a,b):
#     try:
#         return a+b
#     except: return "변수들의 형태가 다릅니다."
# n1=get_sum(10,20)
# print("10과 20의 합=",n1)
# print("100과 200의 합=",get_sum(100,200))
# # 3번
# def print_sub(a,b):
#     try:
#         return print(f"{a}와 {b}의 차는 {a-b}입니다.")
#     except: return print(f"오류 발생! {a}은(는) {type(a).__name__}이고 {b}은(는) {type(b).__name__}입니다.")
# print_sub(10,20)
# print_sub(100,40)
# # 4번
# def greet(name,msg="안녕하세요"):
#     if type(name)==int or type(name)==float or type(name)==complex:
#         return print("숫자는 이름이 아닙니다.")
#     if type(msg)==int or type(msg)==float or type(msg)==complex:
#         return print("숫자는 인사가 아닙니다.")
#     return print(msg,name)
# greet("홍길동")
# greet("이순신","반갑습니다.")
# # 5번
# def sum_and_mul(a,b):
#     try:
#         sum=a+b
#         mul=a*b
#         return sum,mul
#     except:return "오류 발생!","오류 발생!"
# s,m=sum_and_mul(3,4)
# print(f"합: {s}")
# print(f"곱: {m}")
# # 6번
# count=0
# def add_count():
#     global count
#     count+=1

# add_count()
# add_count()
# add_count()
# print(count)
# 7번
# def list_info(numbers=list()):
#     try:
#         print(f"최솟값 :{min(numbers)}")
#         print(f"최댓값 :{max(numbers)}")
#         print(f"합계 :{sum(numbers)}")
#     except:print("이 함수의 변수는 list로 표현가능해야 합니다.")
# list_info([3,5,7,-2,6])
# # 8번
# def sum_nums(*args):
#     sum=0
#     try:
#         for i in args:
#             sum+=i
#         avg=sum/(len(args))
#         print(f"{len(args)} 개의 인자 {args}")
#         print(f"합계 : {sum}, 평균 : {avg}")
#     except: print("숫자형 인자들의 list만 받습니다.")

# sum_nums(10,20,30)
# sum_nums(10,20,30,40,50)
# # 9번
# def print_info(**kwargs):
#     try:
#         for i,j in kwargs.items():
#             print(i,":",j)    
#     except:print("잘못된 변수로 출력 불가")
# print_info(name="홍길동",age=20,major="컴퓨터공학")
# 10번
def report_card(name,*scores,bonus=0):
    sum=0+bonus
    for i in scores:
        sum+=i    
    avg=round(sum/len(scores),1)
    def degree(avg):
        if(avg>=90):return"A등급"
        if(90>avg>=80):return"B등급"
        if(80>avg>=70):return"C등급"
        if(avg<70):return"F등급"
    print(f"학생 : {name}")
    print(f"총점 : {sum}, 평균 : {avg}, 등급 {degree(avg)}")
    return(sum,avg,degree(avg))
total, avg, grade = report_card("홍길동", 85, 90, 78, bonus=5)
total, avg, grade = report_card("이순신", 60, 55, 70)
