def Add(Num1, Num2):
    Sum = 0
    Sum = Num1 + Num2
    return Sum


def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))
    res = Add(Value1, Value2)   
    print("Addition is:", res)
    
if __name__ == "__main__":
    main()