isOdd = lambda num : num %2!=0

Value = int(input("Enter a Number: "))
print(isOdd(Value))
if(isOdd(Value)):
    print("Even Number")
else :
    print("Odd Number")