import os;

def directoryScanner(dirName):
    res = os.path.exists(dirName)
    if res == True:
        print("directory Exists")
    else:
        print("Directory not present")


def main():
    directoryName = input("Enter Directory Name")
    directoryScanner(directoryName)
if __name__ =="__main__":
    main()