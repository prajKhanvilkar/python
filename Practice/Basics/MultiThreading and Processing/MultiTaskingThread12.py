import time
import threading

def SumEven(No):
    sum = 0
    for i in range(2,No+1,2):
        sum = sum + i
    print("Even Sum is :",sum)

def SumOdd(No):
    sum = 0
    for i in range(1,No+1,2):
        sum = sum + i
    print("Odd Sum is :",sum)

def main():
    start = time.time()

    t = threading.Thread(target=SumEven,args=(100000000,))
    t1 = threading.Thread(target=SumOdd,args=(100000000,))

    t.start()
    t1.start()

    t.join()
    t1.join()
    
    end = time.time()
    print("Time Required",end-start)
    

if __name__ == "__main__":
    main()