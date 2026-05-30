import threading

def checkEven(Arrlist):
    sum =0
    for i in Arrlist:
        if i % 2 == 0:
            sum = sum + i
    print(f"Sum of Even numbers is: {sum}")

def checkOdd(Arrlist):
    sum =0
    for i in Arrlist:
        if i % 2 != 0:
            sum = sum + i
    print(f"Sum of Odd numbers is: {sum}")

def main():
    Arraylist = [1,2,3,4,5,6,7,8,9,10]
    t1 = threading.Thread(target=checkEven, args=(Arraylist,))
    t2 = threading.Thread(target=checkOdd, args=(Arraylist,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()