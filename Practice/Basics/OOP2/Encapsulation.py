class Arithematic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        print("Object gets created successfully")

    def Addition(self):
        Ans =0 
        Ans = self.No1 + self.No2
        return Ans
    def Subtraction(self):
        Ans =0 
        Ans = self.No1 - self.No2
        return Ans
    
obj1 = Arithematic(10,11)   
obj2 = Arithematic(21,20)

ret = obj1.Addition()
print("Addition is:",ret)
ret = obj2.Subtraction()
print("Subtraction is:",ret)