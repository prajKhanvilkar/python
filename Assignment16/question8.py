def printNum(number):
    for i in range(1, number + 1):
        print("*")

def main():
    num = int(input("Enter a number: "))
    printNum(num)

if __name__ == "__main__":
    main()