import time
import numpy as np
start=time.time()
arr_a=np.array(list(range(1,10000001)))
arr_b=np.array(list(range(1,10000001)))
result=np.array(list(range(1,10000001)))
for i in range(len(arr_a)):
    result[i]=arr_a[i] * arr_b[i]
end=time.time()
print(f"소요시간 : {end-start}")
# 기본 연산자 시간, 0.014187 초
start1=time.time()
result=arr_a * arr_b
end1=time.time()
print(f"소요시간 : {end1-start1}")
