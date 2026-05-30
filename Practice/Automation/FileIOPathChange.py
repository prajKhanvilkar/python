import os
def main():
    FileName = input("Enter the file name :")
    if os.path.exists(FileName):
        Ret = os.path.isabs(FileName)
        if Ret == True:
            print("Given path is Absolute path")
        else:
            print("Given path is Relative path")
            newPath = os.path.abspath(FileName)
            print("Absolute path is :", newPath)
    else:
        print("There is no such file")
       
if __name__ == "__main__":
    main()
