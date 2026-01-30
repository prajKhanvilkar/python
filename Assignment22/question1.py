class Demo:
    value =1
    def __init__(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def Fun(self):
        print("Inside instance method fun",self.Value1,self.Value2)

    def Gun(self):
        print("Inside instance method fun",self.Value1,self.Value2) 

Obj1 = Demo(10,11)   
Obj2 = Demo(51,101)
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj1.Gun()     