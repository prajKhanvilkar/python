def isPerfect(num):
    Sum = 0
    for i in range(1, num):
        if(num % i == 0):
            Sum = Sum + i
    if (Sum == num):
        print("Number is a Perfect Number.")
    else:
        print("Number is not a Perfect Number.")

num = int(input("Enter a number: "))
isPerfect(num)