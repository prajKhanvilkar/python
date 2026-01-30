class Numbers:

    def __init__(self,v=0):
        V = int(input("Enter a value"))
        self.Value = V

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value/2) + 1):
            if self.Value % i == 0:
                return False
        return True


    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    # Check Perfect
    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False

    # Display all factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()        


obj1 = Numbers()

print("Obj1 Prime:", obj1.ChkPrime())
print("Obj1 Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of factors:", obj1.SumFactors())