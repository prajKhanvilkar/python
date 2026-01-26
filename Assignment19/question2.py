Multiply = lambda x, y: x * y

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    res = Multiply(num1, num2)
    print(f"Multiplication: {res}")
if __name__ == "__main__":
    main()