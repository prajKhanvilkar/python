import threading

def PrintDigits(num):
    for i in range(1,num+1):
        print(i)

def PrintReverseDigits(num):
    for i in range(num,0,-1):
        print(i)

def main():
    t1 = threading.Thread(target=PrintDigits, args=(50,))
    t2 = threading.Thread(target=PrintReverseDigits, args=(50,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()