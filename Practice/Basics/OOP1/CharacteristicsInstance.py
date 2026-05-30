import gc

class Demo:
    #clas variable
    No1 =10
    No2 =12
    def __init__(self):
        #Instance variablex
        self.A = 101
        self.B= 201
        print("inside constructor")
    def __del__(self):
        print("inside destructor")

print(Demo.No1)
print(Demo.No2)

obj = Demo()
print(obj.A)
print(obj.B)