import hashlib
import os


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


def DisplayResult(myDict):
    res = list(filter(lambda x: len(x)>1, myDict.values()))
    count = 0
    for value in res:
        for subValue in value:
            count += 1
            print(f"File {count} : {subValue}")
        print("Value of Count is :", count)
        count = 0

def DeleteDuplicate(path = "Marvellous"):
    myDict = FindDuplicate(path)
    res = list(filter(lambda x: len(x)>1, myDict.values()))
    count = 0
    cnt = 0

    for value in res:
        for subValue in value:
            count += 1
            if count > 1:
                print(f"Deleting file : {subValue}")
                os.remove(subValue)
                cnt += 1
        count = 0
    print(f"Total {cnt} duplicate files removed")   


def main():
    DeleteDuplicate()
    # DisplayResult(ret)
if __name__ == "__main__":                                                                                              
    main()