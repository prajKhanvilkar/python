import sys
import time
import os
import schedule
import shutil
import hashlib

def calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path,"rb")

    while True:
        data =fobj.read(1024)
        if(not data):
            break
        else:
            hobj.update(data)
    fobj.close()
    return hobj.hexdigest()

def BackupFiles(Source,Destination):
    copied_files = []
    print("creating the Backup folder for backup process")
    os.makedirs(Destination,exist_ok=True)
    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)
            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)
            #copy the files if its new or updated
            if(not os.path.exists(dest_path)):
                shutil.copy2(src_path,dest_path)
                copied_files.append(relative)
            
    return copied_files

def marvellousDataShieldStart(Source = "Data"):
    backUpName = "marvellousBackup"

    print("backup process started successfully at", time.ctime())
    files  = BackupFiles(Source,backUpName)
    print("Report About the Backup")
    for name in files:
        print(name+"\n")

    

def main():
    border = "-" * 50
    print(border)
    print("-----------Marvellous Data Shield System----------")
    print(border)
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to")
            print("1: Takes Auto Backup at given time")
            print("2: Backup only new and updated files")
            print("3: create an archive of the backup perioically")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory Name")
            print("TimeInterval: the time in minutes for periodic scheduling")
            print("SourceDirectory Name: Name of SourceDirectory to backedup")

        else: 
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    #python3 Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time Interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])
        #Apply Schedular
        schedule.every(int(sys.argv[1])).minutes.do(marvellousDataShieldStart, sys.argv[2])
        print("Data Shield System Started Successfully")
        print("Time Interval in Minutes: ",sys.argv[1])
        print("Press control + c to stop the execution")
        #wait til abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Command Line Arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

            
    print(border)
    print("---------Thank you fro using our script-----------")
    print(border)

if __name__ =="__main__":
    main()