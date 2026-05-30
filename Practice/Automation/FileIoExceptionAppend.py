def main():
    fobj = None
    try:
        fobj = open("Demo.txt","a")
        print("File gets successfuly opened")
        fobj.write("Welcome to Python Automation")
        fobj.close()
    except FileNotFoundError :
        print("Unable to open file as there is no such file")   
    finally:
        print("End of application")

    
if __name__ == "__main__":
    main()
