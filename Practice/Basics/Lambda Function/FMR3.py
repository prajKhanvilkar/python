from functools import reduce

def checkEven(No):
    return (No %2 ==0)

def Increament(No) : 
    return No +1

def Add(A,B):
   return A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is:",Data)

    FData = list(filter(checkEven,Data))  #Function must return Boolean
    print("Filtered Data is", FData)

    Mdata = list(map(Increament,FData))   #Function must accept one value and return modified value 
    print("Map Data is", Mdata)

    Rdata = reduce(Add,Mdata)
    print("Reduced Data is", Rdata)       #Function must accept 2 value and return 1 modified value 

if __name__ == "__main__":
    main()