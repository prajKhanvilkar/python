import psutil
import time

def createLog():
    border = "-"*50
    timeStamp = time.strftime("%Y_%M_%d_%H_%M_%S")
    fileName = "MarvellousAssignment1%s.log"%timeStamp
    fobj  = open(fileName,"w")
    fobj.write(border+"\n")
    fobj.write("This log File is created by Marvellous Automation"+"\n")
    fobj.write("This is Thread Monitoring Feature"+"\n")
    fobj.write(border+"\n")

    fobj.write("-----------------Process Scan Report--------------"+"\n")
    fobj.write(border+"\n")
    for proc in psutil.process_iter(attrs=['pid','name','num_threads']):
        try:
            pinfo = proc.info
            fobj.write("%s %s %s"%(pinfo["pid"] ,pinfo["name"], pinfo["num_threads"])+"\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    fobj.write(border+"\n")
    fobj.write("---------------- Report Completed-----------------"+"\n")
    fobj.write(border+"\n")
def main():
   createLog()
if __name__ == "__main__":
    main()