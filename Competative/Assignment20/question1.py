import threading

def checkEven():
    for i in range(1, 21):
        if i % 2 == 0:
            print(f"Even: {i}")

def checkOdd():
    for i in range(1, 21):
        if i % 2 != 0:
            print(f"Odd: {i}")

def main():
    t1 = threading.Thread(target=checkEven)
    t2 = threading.Thread(target=checkOdd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()