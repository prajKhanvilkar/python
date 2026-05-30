import hashlib
import os
import sys

def calculate_checksum(FileName):
    fobj = open(FileName, 'rb')
    hobj = hashlib.md5()
    Buffer = fobj.read(1000)
    while (len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):
    ret = False
    ret = os.path.exists(DirectoryName)
    if(ret == False):
        return
    ret = os.path.isdir(DirectoryName)
    if(ret == False):
        return
    
    for Foldername, Subfolders, Filenames in os.walk(DirectoryName):
        for Filename in Filenames:
            Filepath = os.path.join(Foldername, Filename)
            Checksum = calculate_checksum(Filepath)
            print(f"File Name : {Filename} Checksum : {Checksum}")


def main():
    border = "-"*50
    print(border)
    print("-------Marvellous Directory Automation----------")
    print(border)
    if(len(sys.argv)!=2):
        print("Invalid Number of Argument")
        print("Please Specify the Name of the Directory")
        return
    DirectoryWatcher(sys.argv[1])

if __name__ == "__main__":
    main()