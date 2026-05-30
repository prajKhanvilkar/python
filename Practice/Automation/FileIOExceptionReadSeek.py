def main():
    fobj = None
    try:
        fobj = open("Hello.txt","r")
        print("File gets successfuly opened")

        print("Current offset is:",fobj.tell()) #0
        fobj.seek(7)
        print("Current offset is:",fobj.tell()) #7

        data = fobj.read(10)

        print("Current offset is:",fobj.tell()) #17
        print("Data from file is:",data)

        fobj.close()

    except FileNotFoundError :
        print("Unable to open file as there is no such file")   
    finally:
        print("End of application")

    
if __name__ == "__main__":
    main()
