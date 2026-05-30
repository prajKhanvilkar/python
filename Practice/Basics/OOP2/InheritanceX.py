class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
        self.No1 = 10
        self.No2 =20
    def fun(self):
        print("Inside fun method of parent", self.No1,self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")
        self.A = 11
        self.B = 21
    def sun(self):
        print("inside sun method of child", self.A,self.B, self.No1,self.No2)

cObj = Child()
print(cObj.No1)
print(cObj.No2)

print(cObj.A)
print(cObj.B)

cObj.sun()
cObj.fun()