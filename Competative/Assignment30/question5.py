import os;
import sys;
import filecmp;

def directoryScanner(dirName, string):
    res = os.path.exists(dirName)
    if res == False:
        print("Directory not present")
    try:
        fobj = open(dirName,"r")
        data  = fobj.read()
        print("Data in file is:", data)
        if string in data:
            print("has the given value")
        else:
            print("does not have given value")

    except FileNotFoundError: 
        print("unable to open a file as there is no such files")

    fobj.close()
    

def main():
    directoryName = sys.argv[1]
    string = sys.argv[2]
    directoryScanner(directoryName, string)
if __name__ =="__main__":
    main()