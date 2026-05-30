def main():
    fobj = None
    try:
        fobj = open("Demo.txt","r")
        print("File gets successfuly opened")

        data = fobj.read(6)
        print("Data from file is:")
        print(data)

        fobj.close()
    except FileNotFoundError :
        print("Unable to open file as there is no such file")   
    finally:
        print("End of application")

    
if __name__ == "__main__":
    main()
