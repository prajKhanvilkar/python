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
    if(res == True):
        print("Its Even")
    else: 
        print("Its Odd")

if __name__ == "__main__":
    main()