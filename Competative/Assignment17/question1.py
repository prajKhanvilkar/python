import Arithmatic as ar

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    res = ar.Add(num1, num2)
    print(f"Addition: {res}")

    res = ar.Subtract(num1, num2)
    print(f"Subtraction: {res}")    

    res = ar.Multiply(num1, num2)
    print(f"Multiplication: {res}") 

    res = ar.Divide(num1, num2)    
    print(f"Division: {res}")

if __name__ == "__main__":
    main()