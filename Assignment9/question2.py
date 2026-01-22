def ChkGreater(Num1,Num2):
    if(Num1>Num2):
       return Num1
    else:
        return Num2

Inp1 = int(input("Enter first number"))
Inp2 = int(input("Enter second number"))
res = ChkGreater(Inp1,Inp2)
print(res, "is greater")
