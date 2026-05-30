import gc

class Demo:
    def __init__(self):
        print("inside constructor")
    def __del__(self):
        print("inside destructor")
obj = Demo()

del obj
gc.collect()

print("End of Application")
