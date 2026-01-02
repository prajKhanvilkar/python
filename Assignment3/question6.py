from sys import getsizeof
print("Enter A Value")
value = input()
print(type(value)) # data type
print(id(value)) # unique identifier
print(getsizeof(value)) # size in bytes

# Example Outputs:
# Enter A Value
# 100
# <class 'str'>
# 140709353828688
# 53    