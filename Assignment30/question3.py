import os;
import sys;
def directoryScanner(dirName):
    res = os.path.exists(dirName)
    if res == False:
        print("Directory not present")
    try:
        fobj = open(dirName,"r")
        data  = fobj.read()
        print("Data in file is:", data)
    except FileNotFoundError: 
        print("unable to open a file as there is no such files")

    fobj.close()


def main():
    directoryName = sys.argv[1]
    directoryScanner(directoryName)
if __name__ =="__main__":
    main()