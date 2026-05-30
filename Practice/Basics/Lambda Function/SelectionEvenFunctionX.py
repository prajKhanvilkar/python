#Procedural Approach
def checkEven(Num):
    if (Num % 2 == 0 ) :
        print("Its Even")
    else:
        print("Its Odd")

def main():
    Value=0
    Value = int(input("Enter a number:"))
    checkEven(Value) #postional
    #checkEven(Num=22) #Keyword

if __name__ == "__main__":
    main()