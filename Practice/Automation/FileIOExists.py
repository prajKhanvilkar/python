import os
def main():
    FileName = input("Enter the file name :")
    Ret = os.path.exists(FileName)
    if Ret == True:
        fobj = open(FileName, "r")
        print("File Gets Successfully Opened")
    else:
        print("There is no such file")
       
if __name__ == "__main__":
    main()
