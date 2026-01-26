def patter(number):
    for i in range(1,number+1):
            for j in range(1,i):    
                print(j ,end=" ")
            print()
def main():
    val = int(input("Enter a number"))
    patter(val)
if __name__ == "__main__":
    main()