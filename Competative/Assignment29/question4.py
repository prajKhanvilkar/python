import os;
import sys;
import filecmp;

def directoryScanner(dirName, dirName2):
    res = os.path.exists(dirName)
    if res == False:
        print("Directory not present")
    res = os.path.exists(dirName2)
    if res == False:
        print("Directory not present")
    areEqual = filecmp.cmp(dirName,dirName2)
    if areEqual == True:
        print("Files are Equal")
    else:
        print("Files are not equal")

def main():
    directoryName = sys.argv[1]
    directoryName2 = sys.argv[2]
    directoryScanner(directoryName, directoryName2)
if __name__ =="__main__":
    main()