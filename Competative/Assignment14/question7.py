isDivisible = lambda num : num %5==0

Value = int(input("Enter a Number: "))
print(isDivisible(Value))
if(isDivisible(Value)):
    print("Is divisible by 5")
else :
    print("Not divisible by 5")