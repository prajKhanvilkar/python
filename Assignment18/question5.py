import MarvellousNum as MN
def SumofList(data):
    total = 0
    for num in data:
        total += num
    return total
    

def main():
    number1 = int(input("Enter a number for List: "))
    data = list()
    for i in range(number1):
        num = int(input("Enter a number: "))
        if MN.checkPrime(num):
            data.append(num)
    result = SumofList(data)
    print("Updated List:", result)

if __name__ == "__main__":
    main()
