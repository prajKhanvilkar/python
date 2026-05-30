class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
    def fun(self):
        print("Inside fun method of parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")
    def fun(self):
        super().fun()
        print("inside fun method of child")

obj = Child()
obj.fun()