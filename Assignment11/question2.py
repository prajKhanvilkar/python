def count_digits(number):
    number = abs(number)   # handle negative numbers
    count = 0

    if number == 0:
        return 1

    while number > 0:
        number = number // 10  
        count += 1
    return count


num = int(input("Enter a number: "))

print("Count of digits:", count_digits(num))
