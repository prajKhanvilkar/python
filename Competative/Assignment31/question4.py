import os
import sys
import time
import shutil

def directoryScanner(DirName = "Demo", DirName2 = "Marvellous", dirType = ".txt"):  
    border = "-"*50
    timeStamp = time.ctime()
    LogFileName = "marvellousQuestion4_%s.log" %(timeStamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    fobj = open(LogFileName,"w")
    fobj.write(border+"\n")
    fobj.write("This is a log file created by marvellous automation"+"\n")
    fobj.write("This is a Directory cleaner script"+"\n")
    fobj.write(border+"\n")
    if not os.path.exists(DirName2):
        try:
            os.makedirs(DirName2)
            fobj.write(f"Created destination directory: {DirName2}"+"\n")
        except OSError as e:
            fobj.write(f"Error creating destination directory {DirName2}: {e}"+"\n")
            return

    for dirpath, dirnames, filenames in os.walk(DirName):
        relative_path = os.path.relpath(dirpath, DirName)
        destination_path = os.path.join(DirName2, relative_path)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        for filename in filenames:
            if filename.endswith(dirType):
                source_file = os.path.join(dirpath, filename)
                destination_file = os.path.join(destination_path, filename)
                try:
                    shutil.copy2(source_file, destination_file)
                    fobj.write(f"Copied: {source_file} to {destination_file}"+"\n")
                except IOError as e:
                    fobj.write(f"Error copying file {source_file}: {e}"+"\n")
                except Exception as e:
                    fobj.write(f"An unexpected error occurred while copying {source_file}: {e}"+"\n")


    
    fobj.write("----------------Automation Report-----------------"+"\n")
    fobj.write("This log file is Created at:"+timeStamp+"\n")
    fobj.write(border+"\n")

    fobj.close()


def main():
    border = "-"*50
    print(border)
    print("-------Marvellous Directory Automation----------")
    print(border)
    if(len(sys.argv)!=4):
        print("Invalid Number of Argument")
        print("Please Specify the Name of the Directory")
        print("Please Specify the Name of Directory to which you want to copy")
        print("Enter the file extension you want to copy")
        return
    directoryScanner(sys.argv[1],sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()