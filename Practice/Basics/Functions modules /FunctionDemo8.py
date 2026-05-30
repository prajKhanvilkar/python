#Accept :Multiple Parameters
#Return :Multiple Value
def Marvellous1(Value1,Value2): #positional parameters
    print("Inside Marvellous1 ; ",Value1, Value2)
    return 11,21,51

def main():
    result1 = None
    result2 = None
    result3 = None
    result1, result2, result3 = Marvellous1("Python",21)
    print("Return value is : ",result1, result2, result3)
   
if __name__ == "__main__":
    main()