def OddNum(Num):
    Data = list()
    for i in range(1,Num + 1):
        if(i % 2 !=0):
            Data.append(i)
    return Data
inp = int(input("Enter a Number: "))
res= OddNum(inp)
print("Odd list is:", res)