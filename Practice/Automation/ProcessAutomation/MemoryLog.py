import psutil
import sys
import time
import os
import schedule

def CreateLog(FolderName):
    border = "-" * 50
    Ret = False
    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret ==  False):
            print("Unable to create Folder")
            return
    else: 
        os.mkdir(FolderName)
        print("Directory for log files gets created Successfully")
    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    fileName = os.path.join(FolderName,"Marvellous_%s.log" %timeStamp)
    print("Log File created Name as:",fileName)
    fobj = open(fileName,"w")
    fobj.write(border+"\n")
    fobj.write("------Marvellous Platform Surveillance System-----"+"\n")
    fobj.write("Log Created at : "+ time.ctime()+"\n")
    fobj.write(border+"\n")
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(border+"\n")
    fobj.write("-------------------End of Log File---------------"+"\n")
    fobj.write(border+"\n")
    fobj.close()

    print("CPU Usage: ",psutil.cpu_percent())
    mem = psutil.virtual_memory()
    print("Ram usage: ", mem.percent)
def main():
    border = "-" * 50
    print(border)
    print("------Marvellous Platform Surveillance System-----")
    print(border)
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to")
            print("1: Create Automic Log")
            print("2: Executes Periodically")
            print("3: Sends Mail with the log")
            print("4: Stores information about processess")
            print("5: Stores information about CPU")
            print("6: Stores information about RAM usage")
            print("7: Stores information about secondary Storage")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval Directory Name")
            print("TimeInterval: the time in minutes for periodic scheduling")
            print("Directory Name: Name of Directory to create auto logs")

        else: 
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    #python3 Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        # print("Inside projects logic")
        # print("Time Interval : ",sys.argv[1])
        # print("Directory Name : ",sys.argv[2])
        #Apply Schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])
        print("Platform Surveillance System Started Successfully")
        print("Directory Created with Name: ", sys.argv[2])
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