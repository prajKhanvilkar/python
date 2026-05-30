#lambda
Addition = lambda x, y: x + y
Subtraction = lambda x, y: x - y

No1 =0
No2 =0
Ans = 0

No1 = int(input("Enter First Number: "))
No2 = int(input("Enter Second Number: "))

Ans = Addition(No1, No2)
print("Addition is:",Ans)

Ans = Subtraction(No1, No2)
print("Subtraction is:",Ans)