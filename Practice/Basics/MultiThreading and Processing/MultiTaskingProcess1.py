import time
import multiprocessing
import os
def SumEven(No):
    print("PID of SumEven:",os.getpid())    #51
    print("PPID of SumEven:",os.getppid())  #21
    sum = 0
    for i in range(2,No+1,2):
        sum = sum + i
    print("Even Sum is :",sum)

def SumOdd(No):
    print("PID of SumOdd:",os.getpid())     #101
    print("PPID of SumOdd:",os.getppid())   #21
    sum = 0
    for i in range(1,No+1,2):
        sum = sum + i
    print("Odd Sum is :",sum)

def main():
    print("PID of main:",os.getpid())   #21
    print("PPID of main:",os.getppid()) #11
    start = time.time()

    t = multiprocessing.Process(target=SumEven,args=(100000000,))
    t1 = multiprocessing.Process(target=SumOdd,args=(100000000,))

    t.start()
    t1.start()

    t.join()
    t1.join()
    
    end = time.time()
    print("Time Required",end-start)
    

if __name__ == "__main__":
    main()