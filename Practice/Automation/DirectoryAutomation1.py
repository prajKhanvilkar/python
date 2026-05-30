import os
import sys
def DirectoryScan(DirName = "Marvellous"):
    ret = False
    ret = os.path.exists(DirName)
    if (ret == False):
        print("There is no such Directory")
        return
    ret = os.path.isdir(DirName)
    if (ret == False) :
        print("It is not a Directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for file in FileName:
            print("File Name:",file)
    
def main():
    border = "-"*50
    print(border)
    print("---------Marvellous Directory Automation-----------")
    print(border)
    if(len(sys.argv) !=2):
        print("Invalid Number of arguments")
        print("please specify the name of directory")
        return
    DirectoryScan(sys.argv[1])
    
    
if __name__ =="__main__":
    main()