import os
import sys
import time

def directoryScanner(DirName = "Demo", dirType = ".txt"):
    border = "-"*50
    timeStamp = time.ctime()
    LogFileName = "marvellousQuestion1_%s.log" %(timeStamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    fobj = open(LogFileName,"w")
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
        returnZ

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(dirType):
              fobj.write("Total Files Name: "+fname+"\n")
    
    fobj.write("----------------Automation Report-----------------"+"\n")
    fobj.write("This log file is Created at:"+timeStamp+"\n")
    fobj.write(border+"\n")

    fobj.close()


def main():
    border = "-"*50
    print(border)
    print("-------Marvellous Directory Automation----------")
    print(border)
    if(len(sys.argv)!=3):
        print("Invalid Number of Argument")
        print("Please Specify the Name of the Directory")
        print("Please Specify the type of Directory")
        return
    directoryScanner(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()