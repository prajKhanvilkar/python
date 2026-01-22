def Results(num):
    if (num >= 75):
        print("Distinction")
    elif (num >=60):
        print("First Class")
    elif (num >=50):
            print("Second class")
    else :
         print("Fail")

num = int(input("Enter Marks: "))
Results(num)