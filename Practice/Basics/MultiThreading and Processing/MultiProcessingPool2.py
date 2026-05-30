import time
import os
def SumCube(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i**3)
    return sum

def main():
    data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    res=[]
    start = time.time()
    for i in range(len(data)):
        ret = SumCube(data[i])
        res.append(ret)
    end = time.time()
    print(res)
    print("Time Required",end-start)
    
if __name__ == "__main__":
    main()