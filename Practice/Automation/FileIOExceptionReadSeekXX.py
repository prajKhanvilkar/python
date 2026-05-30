#seek(,)
#seek(Kuthe,Kuthun)
# Kuthun :0/1/2
#0:starting
#1:current position
#2:end of file

def main():
    fobj = None
    try:
        fobj = open("Hello.txt","rb")
        print("File gets successfuly opened")

        print("Current offset is:",fobj.tell()) #0
        fobj.seek(6,2)
        print("Current offset is:",fobj.tell()) #11

        data = fobj.read(6)

        print("Current offset is:",fobj.tell()) #17
        print("Data from file is:",data)

        fobj.close()

    except FileNotFoundError :
        print("Unable to open file as there is no such file")   
    finally:
        print("End of application")

    
if __name__ == "__main__":
    main()
