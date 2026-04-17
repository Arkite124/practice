"""
#mysquare.py : 정사각형의 속성을 계산하는 모듈 get_area(length) : 한 변의 길이 가 length
인 정사각형의 면적을 반환 get_peri(length) : 한 변의 길이 가 length 인 정사각형의 둘레를 반
환 set_pos(x, y) : 좌표 (x, y) 에 도형을 위치시킴
"""
xpos,ypos=0,0
def get_area(length):
    """
    모듈: mysquare.py 함수: get_./area(length)
    한 변의 길이 가 length 인 정사각형의 면적을 계산
    """
    area=length**2
    return area
def get_peri(length):
    """
    모듈: mysquare.py 함수 : get_area(length)
    한 변의 길이 가 length 인 정사각형의 면적을 계산
    """
    peri=4*length
    return peri
def set_pos(x,y):

    global xpos,ypos
    xpos,ypos=x,y