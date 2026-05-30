def Multiplication(Value1,Value2):
    Ans=0 #Local variable
    Ans = Value1 * Value2
    return Ans

def Main():
    No1=0
    No2=0
    result=0 #global variable

    No1 =int(input("Enter First Number : "))
    No2 =int(input("Enter Second Number : "))

    result = Multiplication(No1,No2)
    print("Multiplication is :",result)

Main()
print("end")