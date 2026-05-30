def Fact(Num):
    fact = 1
    for i in range(1,Num + 1):
        fact = fact * i
    return fact
inp = int(input("Enter a Number: "))
res= Fact(inp)
print("Factorial is:", res)