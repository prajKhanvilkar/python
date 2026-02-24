import os
def main():
    DirectoryName = input("Enter the Name of directory")
    print("Contents of the directory are:")
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name:",FolderName)
        for subf in SubFolderName:
            print("SubFolder Name:",subf)
        for fName in FileName:
            print("File Name:",fName)

if __name__ == "__main__":
    main()