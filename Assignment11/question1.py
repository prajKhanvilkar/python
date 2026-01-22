def PrimeNum(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
    
inp = int(input("Enter a Number: "))

if PrimeNum(inp):
    print("Is a prime number.")
else:
    print("Is not a prime number.")
