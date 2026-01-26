def sum_of_digits(number):
    sum = 0
    for digit in number:
        if digit.isdigit():
            sum += int(digit)
    return sum

def main():
    num = input("Enter a number: ")

    print("Sum of digits:", sum_of_digits(num))

if __name__ == "__main__":
    main()