class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
l=int(input("enter length : "))
b=int(input("enter breadth : "))
obj=rectangle(l,b)
print("area of rectangle :",obj.area())
print("perimeter of rectangle : ",obj.perimeter())