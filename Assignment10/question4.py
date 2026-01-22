def EvenNum(Num):
    Data = list()
    for i in range(1,Num + 1):
        if(i % 2 ==0):
            Data.append(i)
    return Data
inp = int(input("Enter a Number: "))
res= EvenNum(inp)
print("Even list is:", res)