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
    fobj.write(border+"\n\n")
    fobj.write("\n-----------System Report-------------\n")
    fobj.write("CPU Usage: :%s %%\n"%psutil.cpu_percent())
    fobj.write(border+"\n")
    mem = psutil.virtual_memory()
    fobj.write("Ram usage: %s %%\n"% mem.percent)
    fobj.write(border+"\n")
    fobj.write("\nDisk usage Report\n")
    fobj.write(border+"\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n"%(part.mountpoint,usage.percent))
        except: 
            pass
    fobj.write(border+"\n")
    net= psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write(border+"\n")
    fobj.write("Sent: %.2f MB\n" %(net.bytes_sent / (1024 * 1024)))
    fobj.write("Received: %.2f MB\n" %(net.bytes_recv / (1024 * 1024)))
    fobj.write(border+"\n")

    #process Log

    fobj.write(border+"\n")
    fobj.write("-------------------End of Log File---------------"+"\n")
    fobj.write(border+"\n")
    fobj.close()

def processScan():
    print("processScan Report")
    for proc in psutil.process_iter(attrs=["pid","name","status"]):
        info = proc.info
        print(info["pid"],info["name"],info["status"])

def main():
    processScan()
    return

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