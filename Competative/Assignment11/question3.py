def sum_of_digits(number):
    total = 0
    for digit in number:
            total += int(digit)
    return total

num = input("Enter a number: ")

print("Sum of digits:", sum_of_digits(num))