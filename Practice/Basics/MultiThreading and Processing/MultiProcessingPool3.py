import time
import multiprocessing
import os
def SumCube(No):
    print("Process is running with PID:", os.getpid())
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i**3)
    return sum

def main():
    start = time.time()
    
    data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    res=[]
    pobj = multiprocessing.Pool()
    res = pobj.map(SumCube,data)
    pobj.close()
    pobj.join()
    end = time.time()

    print(res)
    print("Time Required",end-start)
    

if __name__ == "__main__":
    main()