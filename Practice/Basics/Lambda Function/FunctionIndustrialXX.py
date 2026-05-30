#Procedural Approach
def checkEven(Num):
    return (Num % 2 == 0)

def main():
    Value=0
    res = False
    Value = int(input("Enter a number:"))
    res = checkEven(Value)
    if(res == True):
        print("Its Even")
    else: 
        print("Its Odd")

if __name__ == "__main__":
    main()