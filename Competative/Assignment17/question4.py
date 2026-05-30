def SumOfFactor(num):
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            sum=sum+i
    return sum
def main():
    val=int(input("Enter a number"))
    ret=SumOfFactor(val)
    print("Sum of factors is:",ret)
if __name__=="__main__":
    main()