class FourCal:
    count=0
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def sum_num(self):
        result=self.first+self.second
        FourCal.count+=1
        return result
    
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result

m=MoreFourCal(4,2)
a=FourCal(2,3)
b=FourCal(5,9)
b.sum_num()
b.sum_num()
b.sum_num()
a.sum_num()
b.sum_num()
b.sum_num()
b.sum_num()
print(a.sum_num(),b.sum_num(),m.pow(),FourCal.count)