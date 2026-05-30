from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is:",Data)

    FData = list(filter(lambda No : (No %2 ==0),Data)) 

    Mdata = list(map(lambda No : No +1,FData))
    print("Map Data is", Mdata)

    Rdata = reduce(lambda A,B : A+B,Mdata)
    print("Reduced Data is", Rdata)

if __name__ == "__main__":
    main()