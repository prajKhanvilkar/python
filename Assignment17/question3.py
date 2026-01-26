def Fact(n):
    for i in range(1, n):
        n = n * i
    return n

def main():
    num = int(input("Enter a number to find its factorial: "))
    result = Fact(num)
    print("Factorial is :", result)

if __name__ == "__main__":
    main()