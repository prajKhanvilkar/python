class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius=0
        self.Circumference = 0
        self.Area = 0

    def Accept(self):
        self.Radius = float(input("enter Radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print('Radius:',self.Radius)
        print('Area:',self.Area)
        print('Circimference:',self.Circumference)


Obj1 = Circle()   
Obj1.Accept() 
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()              