class BankAccount:
    ROI = 10.5

    def __init__(self,N,A):
        self.Name = N
        self.Amount =A

    def Display(self):
        print(f"{self.Name} balance present is {self.Amount}" )

    def Deposit(self):
        amount = int(input("Enter a amount for deposit")) 
        self.Amount = self.Amount + amount 

    def Withdraw(self):
        withdrawAmount = int(input("Enter a amount for Withdraw")) 
        if(self.Amount > withdrawAmount ):
            self.Amount = self.Amount - withdrawAmount

        else:
            print("Insufficient Balance") 

    def calculateIntrset(self):
        intrest = (self.Amount * BankAccount.ROI) / 100
        return intrest



Obj1 = BankAccount("ABC",500)
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
Obj1.Display()
print(Obj1.calculateIntrset())