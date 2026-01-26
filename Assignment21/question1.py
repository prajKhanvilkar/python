import threading

def PrimeNum(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
    

def checkPrime(Arrlist):
    for i in Arrlist:
       if PrimeNum(i):
            print(f"Prime number is: {i}")
            
def CheckNonPrime(Arrlist):
    for i in Arrlist:
        if not PrimeNum(i):
                print(f"Non Prime number is: {i}")
            
def main():
    Arraylist = [1,2,3,4,5,6,7,8,9,10]
    t1 = threading.Thread(target=checkPrime, args=(Arraylist,))
    t2 = threading.Thread(target=CheckNonPrime, args=(Arraylist,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()