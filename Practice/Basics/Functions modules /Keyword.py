def Employee(Name,Age,Salary,City) :
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():
    #Positional
    #Employee("Rahul",26,2000.5,"Pune") #correct
    #Employee(26,2000.5,"Rahul","Pune") #wrong
    #Keyword
    Employee(Age = 26,Salary = 2000.5,Name = "Rahul", City = "Pune")
 
    
if __name__ == "__main__":
    main()