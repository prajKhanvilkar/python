def SumCube(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i*i*i) #i**3 ->  power operator
    return sum

def main():
   ret =SumCube(10)
   print(ret)

if __name__ == "__main__":
    main()