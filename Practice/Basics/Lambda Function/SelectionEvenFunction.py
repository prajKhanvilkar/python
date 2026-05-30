#procedural Approach
def checkEven(Num):
    if (Num % 2 == 0 ) :
        print("Its Even")
    else:
        print("Its Odd")

def main():
    #No = int(input("Enter a number:"))
    checkEven(21) #postional
    checkEven(Num=22) #Keyword

if __name__ == "__main__":
    main()