class Arithmatic:

    def __init__(self,A=0,B=0):
        self.Value1 = A
        self.Value2 = B

    def Accept(self):
        Value1 = int(input("Enter Value one: "))
        Value2 = int(input("Enter value Two: "))

        self.Value1 = Value1
        self.Value2 = Value2

    def Addition(self):
        return self.Value1 + self.Value2 

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2
    
Obj1 = Arithmatic()
Obj1.Accept()
print(Obj1.Addition())
print(Obj1.Substraction())
print(Obj1.Multiplication())
print(Obj1.Division())