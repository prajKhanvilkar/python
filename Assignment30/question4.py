import os;
import sys;
def directoryScanner(dirName,dirName2):
    res = os.path.exists(dirName)
    if res == False:
        print("Directory not present")
        res = os.path.exists(dirName2)
    if res == False:
        print("Directory not present")
    try:
        fobj = open(dirName,"r")
        data  = fobj.read()
        fobj1 = open(dirName2,"w")
        fobj1.write(data)
        print("Data printed in the new")
        fobj.close()
        fobj1.close()
    except FileNotFoundError: 
        print("unable to open a file as there is no such files")

   


def main():
    directoryName = sys.argv[1]
    directoryName2 = sys.argv[2]
    directoryScanner(directoryName, directoryName2)
if __name__ =="__main__":
    main()