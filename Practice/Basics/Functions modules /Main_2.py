def Multiplication(Value1,Value2):
    Ans=0
    Ans = Value1 * Value2
    return Ans

def Main():
    No1=0
    No2=0
    result=0 
    No1 =int(input("Enter First Number : "))
    No2 =int(input("Enter Second Number : "))

    result = Multiplication(No1,No2)
    print("Multiplication is :",result)

 #starter   
if __name__ == "__main__":
    Main()