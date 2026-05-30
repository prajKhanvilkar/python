No = 11 #Global

def fun():
    No = 21 #Local
    print("Value of No From fun is :", No) #21

print("Value of No is :",No) #11
fun()
