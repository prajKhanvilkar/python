import psutil
import sys
import time
import os
import schedule
import operator
import smtplib
from email.message import EmailMessage



def CreateLog(FolderName, EmailAddress=None):
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
    data = processScan()
    for info in data:
        fobj.write("pid: %s\n"%info.get("pid"))
        fobj.write("Name: %s\n"%info.get("name"))
        fobj.write("Username: %s\n"%info.get("username"))
        fobj.write("Status: %s\n"%info.get("status"))
        fobj.write("Start Time: %s\n"%info.get("create_time"))
        #  fobj.write("CPU %% : %0.2f \n"%info.get("cpu_percent"))
        fobj.write("Memory %%: %0.2f \n"%info.get("memory_percent"))
        fobj.write("Number of Threads: %s\n"%info.get("num_threads"))
        try:
            process  = psutil.Process(info.get("pid"))
            openFiles = process.open_files()
            fileCount = len(openFiles)
            fobj.write("Number of files open for process ID:%s"%(fileCount)+"\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        fobj.write(border+"\n")
   
    #Process Scan top 10 memory consuming process
    top_processes = get_top_memory_processes(10)
    fobj.write(f"{'PID':<10} | {'Name':<25} | {'RSS (MB)':<15} | {'VMS (MB)':<15} | {'Mem %':<8}\n")
    fobj.write("-" * 80 + "\n")
    for proc in top_processes:
        rss_mb = format_bytes(proc['rss'])
        vms_mb = format_bytes(proc['vms'])
        mem_percent = f"{proc['mem_percent']:.2f}%"
        fobj.write(f"{proc['pid']:<10} | {proc['name']:<25} | {rss_mb:<15} | {vms_mb:<15} | {mem_percent:<8}\n")
    fobj.write(border+"\n")
    
    fobj.write("-------------------End of Log File---------------"+"\n")
    fobj.write(border+"\n")
    fobj.close()
    sender_email = "pkhanvilkar2809@gmail.com"  # Replace with your email
    app_password = "zxbrfnadzkihzkgj"  # Replace with your app password
    receiver_email = sys.argv[3]
    subject = "Marvellous Platform Surveillance System Log"
    body = "Please find the attached log file from Marvellous Platform Surveillance System."
    send_email(sender_email, app_password, receiver_email, subject, body, fileName)

def processScan():
    listProcess = []

    #warmup for cpu percent
    for proc in psutil.process_iter():
        try:
            info = proc.cpu_percent
        except:
            pass

    time.sleep(0.2)

    print("processScan Report")
    for proc in psutil.process_iter():
        try: 
            info = proc.as_dict(attrs=["pid","name","username","status","create_time","num_threads",'memory_info'])
            #convert create time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"
            info["cpu_precent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            listProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listProcess


def get_top_memory_processes(n=10):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'memory_percent']):
        try:
            # Get memory info as a named tuple
            mem_info = proc.memory_info()
            # Append process details to the list
            processes.append({
                'pid': proc.pid,
                'name': proc.info['name'],
                'rss': mem_info.rss,  # Real memory (Resident Set Size)
                'vms': mem_info.vms,  # Virtual memory (Virtual Memory Size)
                'mem_percent': proc.info['memory_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Sort processes by RSS memory in descending order
    processes.sort(key=operator.itemgetter('rss'), reverse=True)
    return processes[:n]

def format_bytes(bytes_val):
    """
    Helper function to convert bytes to a human-readable format (MB).
    """
    return f"{bytes_val / (1024 * 1024):.2f} MB"

def send_email(sender, app_password, receiver, subject, body, log_file):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(body)

    # Attach log file
    with open(log_file, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='octet-stream',
            filename=os.path.basename(log_file)
        )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)

    print("Email sent successfully!")
   

def main():
    border = "-" * 50
    print(border)
    print("------Marvellous Platform Surveillance System-----")
    print(border)
    if(len(sys.argv)==3):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to")
            print("1: Create Automic Log")
            print("2: Executes Periodically")
            print("3: Sends Mail with the log")
            print("4: Stores information about processess")
            print("5: Stores information about CPU")
            print("6: Stores information about RAM usage")
            print("7: Stores information about secondary Storage")
            print("8: Stores information about Network usage")
            print("9: Stores information about top 10 memory consuming processess")
            print("10: Stores information about number of files opened by processess")
            print("11: Stores information about number of threads used by processess")
            print("12: sends email to the receiver with log file attached")


        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval Directory Name")
            print("TimeInterval: the time in minutes for periodic scheduling")
            print("Directory Name: Name of Directory to create auto logs")
            print("Receiver Email: Email of the receiver of the log")

        else: 
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    #python3 Demo.py 5 Marvellous test@gmail.com
    elif(len(sys.argv) == 4):
        #Apply Schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2],sys.argv[3])
        print("Platform Surveillance System Started Successfully")
        print("Directory Created with Name: ", sys.argv[2])
        print("Time Interval in Minutes: ",sys.argv[1])
        print("Receiver Email: ",sys.argv[3])
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