def is_palindrome(number):
    original = number
    number = abs(number)
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return original == reverse

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
