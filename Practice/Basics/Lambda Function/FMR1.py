def checkEven(No):
    return (No %2 ==0)


def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is:",Data)

    FData = list(filter(checkEven,Data))  #Function must return Boolean
    print("Filtered Data is", FData)

if __name__ == "__main__":
    main()