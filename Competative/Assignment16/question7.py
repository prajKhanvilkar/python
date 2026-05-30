def DivisibleBy5(number):
    if number % 5 == 0:
        return True
    else:
        return False    

def main():
    num = int(input("Enter a number: "))
    if DivisibleBy5(num):
        print(num,"is divisible by 5.")
    else:
        print(num,"is not divisible by 5.")

if __name__ == "__main__":
    main()