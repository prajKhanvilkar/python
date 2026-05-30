iCnt = 0
def Update():
    global iCnt
    
    for _ in range(200000):
        iCnt = iCnt + 1
    

def main():
    global iCnt
    Update()
    Update()
    print("value of icnt is :",iCnt)
    

if __name__ == "__main__":
    main()