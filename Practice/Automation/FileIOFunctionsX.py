import os
def main():
    FileName = input("Enter the file name :") #Demo.txt
    if os.path.exists(FileName):
        fobj = open(FileName, 'w')
        print(fobj.readable()) #True
        print(fobj.writable()) #False
        print(fobj.seekable()) #True
        fobj.close()
    else:
        print("There is no such file")
       
if __name__ == "__main__":
    main()
