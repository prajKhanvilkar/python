Data = list()
def MultiplicationTable(Num):
    for i in range(1,11):
        Data.append(Num * i)
    return Data
Inp = int(input("Enter a Number: "))
res = MultiplicationTable(Inp)
print(res)