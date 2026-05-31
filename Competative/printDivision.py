def ChkMod(Num): 
    if Num %3 ==0 and Num %5 ==0:
        return "Divisible by 3 and 5"
    else:
        return "Not divisible by 3 and 5"
Inp = int(input("Enter a number"))
res = ChkMod(Inp)
print(res)
