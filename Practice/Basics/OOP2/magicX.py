#Dunder method/ Magic method/ Special method

class Demo:
    def __init__(self,A):
        self.No = A
    def __add__(self, other):  # Overloading + operator called as magic method or deunder method
        print("Inside __add__ method")
        return self.No + other.No
    def __sub__(self, other):  # Overloading + operator called as magic method or deunder method
        print("Inside __sub__ method")
        return self.No - other.No
    def __mul__(self, other):  # Overloading + operator called as magic method or deunder method
        print("Inside __mul__ method")
        return self.No * other.No
    def __truediv__(self, other):  # Overloading + operator called as magic method or deunder method
        print("Inside __div__ method")
        return self.No / other.No

obj1 = Demo(11)
obj2 = Demo(21)

# print(11+21)        #32
print(obj1 + obj2)  # __add__(onj1, obj2)  => 32 
print(obj1 - obj2)  # __sub__(onj1, obj2)  => -10
print(obj1 * obj2)  # __mul__(onj1, obj2)  => 231
print(obj1 / obj2)  # __truediv__(onj1, obj2)  => 0.5238095238095238
