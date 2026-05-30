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
    fileCount = 0
    emptyFileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fileCount = fileCount+1
            fname = os.path.join(FolderName,fname)
            print("File Name:",fname)
            print("File Size:",os.path.getsize(fname))
            if(os.path.getsize(fname) == 0 ):
                emptyFileCount = emptyFileCount +1
                os.remove(fname)
    border = "-"*50
    print(border)
    print("----------------Automation Report-----------------")
    print("Total Files Scannned",fileCount)
    print("Total Empty File Count",emptyFileCount)
    print(border)

def main():
    border = "-"*50
    print(border)
    print("---------Marvellous Directory Automation----------")
    print(border)
    if(len(sys.argv) !=2):
        print("Invalid Number of arguments")
        print("please specify the name of directory")
        return
    DirectoryScan(sys.argv[1])
    
    print(border)
    print("---------Marvellous Directory Automation----------")
    print(border)
    
if __name__ =="__main__":
    main()