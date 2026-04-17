langs=["한국어","English"]
for i, lang in enumerate(langs):
    u=i+1
    print(f"{u},{lang}")
try: 
    u=(int(input("언어를 선택하세요"))-1)
    if u <0 or u >(len(langs)):
        raise Exception
    print(f"사용자 선택{u+1}:{langs[u]}")
except Exception as e:
    print(f"오류 : {e}")