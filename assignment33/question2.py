import psutil
import time

def createLog():
    border = "-"*50
    timeStamp = time.strftime("%Y_%M_%d_%H_%M_%S")
    fileName = "MarvellousAssignment2%s.log"%timeStamp
    fobj  = open(fileName,"w")
    fobj.write(border+"\n")
    fobj.write("This log File is created by Marvellous Automation"+"\n")
    fobj.write("This is Open File Monitoring Feature"+"\n")
    fobj.write(border+"\n")

    fobj.write("-----------------Process Scan Report---------------"+"\n")
    fobj.write(border+"\n")
    for proc in psutil.process_iter(attrs=['pid','name']):
        try:
            pinfo = proc.info
            process  = psutil.Process(pinfo["pid"])
            openFiles = process.open_files()
            fileCount = len(openFiles)
            fobj.write("%s %s %s"%(pinfo["pid"] ,pinfo["name"], fileCount)+"\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    fobj.write(border+"\n")
    fobj.write("--------------- Report Completed------------------"+"\n")
    fobj.write(border+"\n")
def main():
   createLog()
if __name__ == "__main__":
    main()