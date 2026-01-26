import threading

def SumOfEvenFactors(num):
    sum = 0
    for i in range(1,num+1):
        if(num %i ==0 and i %2==0):
            sum = sum + i

    print(f"Sum of even factors of {num} is: {sum}")

def SumOfOddFactors(num):
    sum = 0
    for i in range(1,num+1):
        if(num %i ==0 and i %2!=0):
            sum = sum + i

    print(f"Sum of odd factors of {num} is: {sum}")

def main():
    val = int(input("Enter a number: "))

    t1 = threading.Thread(target=SumOfEvenFactors, args=(val,))
    t2 = threading.Thread(target=SumOfOddFactors, args=(val,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()
