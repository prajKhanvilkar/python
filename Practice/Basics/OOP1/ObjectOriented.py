#class
class Arithmatic:
    def Addition(self, x, y):
        return x + y

    def Subtraction(self,x, y):
        return x - y

No1 =0
No2 =0
Ans = 0

No1 = int(input("Enter First Number: "))
No2 = int(input("Enter Second Number: "))

Ans = Arithmatic().Addition(No1, No2)
print("Addition is:",Ans)

Ans = Arithmatic().Subtraction(No1, No2)
print("Subtraction is:",Ans)