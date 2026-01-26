def CheckNumber(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

    
def main():
    number = float(input("Enter a number: "))
    result = CheckNumber(number)
    print("The number is", result)

if __name__ == "__main__":
        main()