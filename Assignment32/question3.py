import hashlib
import os
import sys
import time

def calculate_checksum(FileName):
    fobj = open(FileName, 'rb')
    hobj = hashlib.md5()
    Buffer = fobj.read(1000)
    while (len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
    ret = False
    ret = os.path.exists(DirectoryName)
    if(ret == False):
        return
    ret = os.path.isdir(DirectoryName)
    if(ret == False):
        return
    Duplicate = {} 
    for Foldername, Subfolders, Filenames in os.walk(DirectoryName):
        for Filename in Filenames:
            Filename = os.path.join(Foldername, Filename)
            Checksum = calculate_checksum(Filename)
            if Checksum in Duplicate:
                Duplicate[Checksum].append(Filename)
            else:
                Duplicate[Checksum] = [Filename]
    return Duplicate

def DeleteDuplicate(path = "Marvellous"):
    border = "-"*50
    timeStamp = time.ctime()
    LogFileName = "logQuestion3_%s.txt" %(timeStamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    fobj = open(LogFileName,"w")
    fobj.write(border+"\n")
    fobj.write("This is a log file created by marvellous automation"+"\n")
    fobj.write("This is a Directory cleaner script"+"\n")
    fobj.write(border+"\n")
    myDict = FindDuplicate(path)
    res = list(filter(lambda x: len(x)>1, myDict.values()))
    count = 0
    cnt = 0

    for value in res:
        for subValue in value:
            count += 1
            if count > 1:
                fobj.write(f"Deleting file : {subValue}"+"\n")
                os.remove(subValue)
                cnt += 1
        count = 0
    fobj.write(f"Total {cnt} duplicate files removed")   
    fobj.write("----------------Automation Report-----------------"+"\n")
    fobj.write("This log file is Created at:"+timeStamp+"\n")
    fobj.write(border+"\n")

    fobj.close()

def main():
    border = "-"*50
    print(border)
    print("-------Marvellous Directory Automation----------")
    print(border)
    if(len(sys.argv)!=2):
        print("Invalid Number of Argument")
        print("Please Specify the Name of the Directory")
        return
    DeleteDuplicate(sys.argv[1])
   
if __name__ == "__main__":
    main()