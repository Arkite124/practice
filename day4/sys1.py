import sys

# args=sys.argv[1:]
# print(args)
# for i in args:
#     print(i)
if len(sys.argv) > 1:
    filename=sys.argv[1]
    files=open(filename,'r',encoding='utf-8')
    text_str=files.read()
    print(text_str)