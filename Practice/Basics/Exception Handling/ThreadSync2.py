import threading
def Update():
    global iCnt
    
    for _ in range(200000):
        iCnt += 1
    

if __name__ == "__main__":
    iCnt = 0
    t1 = threading.Thread(target=Update)
    t2 = threading.Thread(target=Update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("value of icnt is :",iCnt)