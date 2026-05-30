def pattern(number):
    for  i in range(number,1,-1):
        print("* " * i)

def main():
    value = int(input("Enter a number"))
    pattern(value)

if __name__ == "__main__":
    main()
