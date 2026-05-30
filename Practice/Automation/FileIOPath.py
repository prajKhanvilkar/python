import os
def main():
    FileName = input("Enter the file name :")
    Ret = os.path.isabs(FileName)
    if Ret == True:
        print("Given path is Absolute path")
    else:
        print("Given path is Relative path")
       
if __name__ == "__main__":
    main()
