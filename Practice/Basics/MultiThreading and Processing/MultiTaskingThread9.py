import threading

def Display(No,No1,No2):
    print("Inside Display:",No, No1, No2)

def main():
    t = threading.Thread(target=Display,args=(11,12,21))
    t.start()
    
if __name__ == "__main__":
    main()