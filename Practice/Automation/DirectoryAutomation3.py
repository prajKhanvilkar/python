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
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            print("File Name:",fname)
            print("File Size:",os.path.getsize(fname))
    
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