
def Add (value):
    sum = 0
    for i in range(len(value)):
        sum = sum+ value[i]
    return sum

def main():
    size = 0
    value = 0
    ret = 0
    print("enter the number of elements:")
    size= int(input())
    Data = list()
    print("enter the elements")
    for i in range(size):
        value =int(input())
        Data.append(value)
    ret = Add(Data)
    # print(Data)
    print("Summation is :",ret)

if __name__ == "__main__":
    main()