class AddCalculator:
    def __init__(self,init_value):
        self.value=init_value
    def add(self,val):
        self.value+=val
class UpgradeCalculator(AddCalculator):
    def minus(self,val):
        self.value-=val

cal=UpgradeCalculator(5)
cal.minus(3)
print(cal.value)