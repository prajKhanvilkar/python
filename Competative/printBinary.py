def printBinary(n):
    res = ""
    while n > 0:
        res = str(n & 1) + res
        n >>= 1
    print(res)

num = int(input("Enter a number: "))
printBinary(num)