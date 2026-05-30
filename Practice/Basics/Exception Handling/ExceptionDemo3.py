def main():
    Ans =0
    try : 
        print("Inside Try")
        print("Enter First Number")
        No1 = int(input())
        print("Enter Second Number")
        No2 = int(input())
        Ans = No1/No2
    #except ValueError as vobj: 
       # print("Inside Value Except:",vobj)
    #except ZeroDivisionError as zobj: 
        #print("Inside Zero Except:",zobj)
    except Exception as eobj:
        print ("Inside Exception :",eobj)
    finally:
        print("Inside Finally")
        
    print("Division is :", Ans)

if __name__ == "__main__":
    main()