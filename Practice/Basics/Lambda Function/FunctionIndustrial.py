#Procedural Approach
def checkEven(Num):
    if (Num % 2 == 0 ) :
        return True
    else:
        return False

def main():
    Value=0
    res = False
    Value = int(input("Enter a number:"))
    res = checkEven(Value)
    print(res)

if __name__ == "__main__":
    main()