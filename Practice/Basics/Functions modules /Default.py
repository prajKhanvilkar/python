def Employee(Name,Age,Salary,City = "Pune") :
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():
    #default
    Employee(Age = 26,Salary = 2000.5,Name = "Rahul")
    #default
    #Employee("Rahul",26,2000.5)
 
    
if __name__ == "__main__":
    main()