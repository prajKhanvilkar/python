def main():
    Ans =0
    try : 
        print("Enter First Number")
        No1 = int(input())
        print("Enter Second Number")
        No2 = int(input())
    
        print("Inside Try")
        Ans = No1/No2
    except: 
        print("Inside Except")
    finally:
        print("Inside Finally")
        
    print("Division is :", Ans)

if __name__ == "__main__":
    main()