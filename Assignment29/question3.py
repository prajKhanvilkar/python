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
        fobj1 = open("Demo.txt","w")
        fobj1.write(data)
        print("Data printed in the new")
        fobj.close()
        fobj1.close()
    except FileNotFoundError: 
        print("unable to open a file as there is no such files")

def main():
    directoryName = sys.argv[1]
    directoryScanner(directoryName)
if __name__ =="__main__":
    main()