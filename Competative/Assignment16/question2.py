def ChkNum(Num):
    if Num %2 ==0:
        print("Even Number")
    else:
        print("Odd Number") 

def main():
    Value = int(input("Enter a Number: "))
    ChkNum(Value)   

if __name__ == "__main__":
    main()

