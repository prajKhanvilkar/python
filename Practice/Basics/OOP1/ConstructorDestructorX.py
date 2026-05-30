import gc

class Demo:
    def __init__(self):
        print("inside constructor")
    def __del__(self):
        print("inside destructor")
#allocate
obj1 = Demo()
obj2 = Demo()

#use

#deallocate
del obj1
del obj2

gc.collect()

print("End of Application")
