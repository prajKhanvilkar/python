class Demo:
    No = 10

    def __init__(self, A,B):
        self.Value1 = A
        self.Value2 = B

    def fun(self):
        print("Inside Instance method fun", self.Value1,self.Value2)
    @classmethod
    def sun(cls):
        print("Inside Class Method sun",cls.No)
    @staticmethod
    def gun():
        print("Inside Class Method gun", Demo.No)

Demo.sun()
print("Class Variable No:", Demo.No)

obj = Demo(10,11)
obj.fun()
print("Instance variable of obj1", obj.Value1, obj.Value2)

Demo.gun()