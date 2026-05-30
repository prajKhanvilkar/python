import os
import sys
import time
def DirectoryScan(DirName = "Marvellous"):
    border = "-"*50
    timeStamp = time.ctime()
    fobj = open("Marvellous.log","w")
    fobj.write(border+"\n")
    fobj.write("This is a log file created by marvellous automation"+"\n")
    fobj.write("This is a Directory cleaner script"+"\n")
    fobj.write(border+"\n")
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
            # fobj.write("File Name:",fname)
            # fobj.write("File Size:",os.path.getsize(fname))
            if(os.path.getsize(fname) == 0 ):
                emptyFileCount = emptyFileCount +1
                os.remove(fname)
    
    # fobj.write(border+"\n")
    fobj.write("----------------Automation Report-----------------"+"\n")
    fobj.write("Total Files Scannned"+str(fileCount)+"\n")
    fobj.write("Total Empty File Count"+str(emptyFileCount)+"\n")
    fobj.write("This log file is Created at:"+timeStamp+"\n")
    fobj.write(border+"\n")

    fobj.close()

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