checkEven = lambda No : (No %2 ==0)
Increament = lambda No : No +1
Add = lambda A,B : A+B

def filterx(Task, Elements):
    result = list()
    for no in Elements:
        ret = Task(no)
        if(ret == True):
            result.append(no)  
    return result

def mapx(Task,Element):
    result =list()
    for no in Element:
        ret = Task(no)
        result.append(ret)
    return result   

def reducex(Task,Element):
    sum = 0
    for no in Element:
         sum = Task(sum,no)
    return sum  


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