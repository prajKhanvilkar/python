import threading

def SmallCase(string):
    count =0
    for i in string:
        if i.islower(): 
            count = count +1
    print(f"Number of small case letters: {count}")

def CapitalCase(string):
    count =0
    for i in string:
        if i.isupper(): 
            count = count +1
    print(f"Number of capital case letters: {count}")

def digits(string):
    count =0
    for i in string:
        if i.isdigit(): 
            count = count +1
    print(f"Number of digits: {count}")

def main():
    string = input("Enter a string: ")

    t1 = threading.Thread(target=SmallCase, args=(string,))
    t2 = threading.Thread(target=CapitalCase, args=(string,))
    t3 = threading.Thread(target=digits, args=(string,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()