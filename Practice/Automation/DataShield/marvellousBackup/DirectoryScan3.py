import os
def DirectoryScanner(DirectoryName = "Marvellous"):
    ret = os.path.exists(DirectoryName)
    if ret == False:
        print("There is no shuch Directory")
        return
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("unable to scan as its not a directory")
        return
    
    print("Contents of the directory are:")
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name:",FolderName)
        for subf in SubFolderName:
            print("SubFolder Name:",subf)
        for fName in FileName:
            print("File Name:",fName)

def main():
    DirectoryName = input("Enter the Name of directory")
    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()