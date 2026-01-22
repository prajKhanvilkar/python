def sum_of_digits(number):
    number = abs(number) 
    total = 0

    while number > 0:
        digit = number % 10     
        total += digit          
        number = number // 10    

    return total

num = int(input("Enter a number: "))

print("Sum of digits:", sum_of_digits(num))