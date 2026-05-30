from FMRModule import filterx,mapx,reducex;

checkEven = lambda No : (No %2 ==0)
Increament = lambda No : No +1
Add = lambda A,B : A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is:",Data)

    FData = list(filterx(checkEven,Data))  #Function must return Boolean
    print("Filtered Data is", FData)

    Mdata = list(mapx(Increament,FData))
    print("Map Data is", Mdata)

    Rdata = reducex(Add,Mdata)
    print("Reduced Data is", Rdata)

if __name__ == "__main__":
    main()