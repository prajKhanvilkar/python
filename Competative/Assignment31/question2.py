import os
import sys
import time

def directoryScanner(DirName = "Demo", dirType = ".txt", dirType2 = ".doc"):
    border = "-"*50
    timeStamp = time.ctime()
    LogFileName = "marvellousQuestion2_%s.log" %(timeStamp)
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
        return

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(dirType):
                old_path = os.path.join(FolderName, fname)
                base, ext = os.path.splitext(fname)
                if ext == dirType:
                    new_filename = base + dirType2
                    new_path = os.path.join(FolderName, new_filename)
                    
                    try:
                        os.rename(old_path, new_path)
                        fobj.write(f"Renamed: {old_path} -> {new_path}"+"\n")
                    except OSError as e:
                        fobj.write(f"Error renaming file {old_path}: {e}")

    
    fobj.write("----------------Automation Report-----------------"+"\n")
    fobj.write("This log file is Created at:"+timeStamp+"\n")
    fobj.write(border+"\n")

    fobj.close()


def main():
    border = "-"*50
    print(border)
    print("-------Marvellous Directory Automation----------")
    print(border)
    if(len(sys.argv)!=4):
        print("Invalid Number of Argument")
        print("Please Specify the Name of the Directory")
        print("Please Specify the type of Directory")
        print("Please Specify the type of Directory you want to convert to")
        return
    directoryScanner(sys.argv[1],sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()