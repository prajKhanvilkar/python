def reverse_number(number):
    number = abs(number) 
    reverse = 0

    while number > 0:
        digit = number % 10       
        reverse = reverse * 10 + digit
        number = number // 10  

    return reverse

# Input from the user
num = int(input("Enter a number: "))

rev = reverse_number(num)

print("Reversed number:", rev)