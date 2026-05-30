
def main():
    size = 0
    value = 0
    sum=0
    print("enter the number of elements:")
    size= int(input())
    Data = list()
    print("enter the elements")
    for i in range(size):
        value =int(input())
        Data.append(value)
    # print(Data)

    for i in range(size):
        sum = sum+ Data[i]
    
    print("Summation is :",sum)

if __name__ == "__main__":
    main()