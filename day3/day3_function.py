# def print_star(a):
#     try:
#         print("*"*int(a))
#     except:
#         print(f"{a}이(가) 숫자가 아닙니다.")
#     return 0

# def get_sum(a,b):
#     try:
#         return print(a+b)
#     except: return print("오류발생! 잘못된 연산입니다.")

# get_sum("1","2")
# get_sum(1,"2")
# get_sum("1",2)
# get_sum(1,2)
# get_sum("1","2")

# def get_root(a, b, c):
#     r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
#     r2 = (-b - (b ** 2 - 4 * a * c) **0.5)/ (2 * a)
#     return r1, r2

# result1, result2 = get_root(1, 2, -8)
# print('해는', result1, '또는', result2)
def is_odd(num):
    try:
        if num%2==0:print(f"{num}은 짝수입니다.")
        else : print(f"{num}은 홀수입니다")
    except: print(f"{num}은(는) 숫자가 아닙니다.")

def sum_nums(*nums):
    try:
        counts = len(nums)
        for n in nums:
            sum+=n
        avg=sum/counts
        print (f"숫자들의 평균은 {avg}입니다.")
    except:print("잘못된 값을 입력했습니다.")

def gugudan(num):
    try:
        if(1<num<10 and type(num)==int):
            for i in range(9):
                print(f"{num}x{i+1}은(는) {(i+1)*num}")
        else : print(f"{num}은(는) 계산 범위를 벗어났습니다.")
    except:print(f"{num}은(는) 숫자가 아닙니다.")
gugudan(9)