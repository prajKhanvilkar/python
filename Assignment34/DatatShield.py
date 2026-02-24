import smtplib
import sys
import time
import os
import schedule
import shutil
import hashlib
import zipfile
from email.message import EmailMessage

DEFAULT_EXCLUDED_EXTENSIONS = {'.temp', '.log', '.exe'}

def make_zip(folderName):
    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folderName+"_"+timeStamp+".zip"
    #open the Zip file
    zobj = zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED)
    for root, dirs,files in os.walk(folderName):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folderName)
            zobj.write(full_path,relative)
    zobj.close()
    return zip_name

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

def BackupFiles(Source, Destination, excluded_ext=None):
    copied_files = []

    # Merge default + user defined exclusions
    if excluded_ext is None:
        excluded_ext = set()
    excluded_ext = DEFAULT_EXCLUDED_EXTENSIONS.union(
        {ext.lower() for ext in excluded_ext}
    )

    print("Creating Backup folder...")
    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):

        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in excluded_ext:
                continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy only new or modified files
            if (not os.path.exists(dest_path)) or (
                calculate_hash(src_path) != calculate_hash(dest_path)
            ):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files

def marvellousDataShieldStart(Source = "Data", user_exclusions=None):
    border = "-" * 50
    backUpName = "marvellousBackup"

    print(border)
    print("backup process started successfully at", time.ctime())
    print(border)
    files  = BackupFiles(Source,backUpName, excluded_ext=user_exclusions)
    zip_file = make_zip(backUpName)
    print(border)
    print("Backup completed Successfully")
    print("Files Copied:", len(files))
    print("Zip Files get created:", zip_file)
    update_backup_history(zip_file, len(files))
    print(border)
    create_log_file(files,zip_file)

def create_log_file(files,zip_file):
    Ret = False
    Ret = os.path.exists("marvellousLogs")
    if(Ret == True):
        Ret = os.path.isdir("marvellousLogs")
        if(Ret ==  False):
            print("Unable to create Folder")
            return
    else: 
        os.mkdir("marvellousLogs")
        print("Directory for log files gets created Successfully")
    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    fileName = os.path.join("marvellousLogs","marvellousDataShield%s.log" %timeStamp)
    print("Log File created Name as:",fileName)
    log_file_name = fileName
    with open(log_file_name,"a") as fobj:
        fobj.write("Backup Time: "+time.ctime()+"\n")
        fobj.write("Files Copied: "+str(len(files))+"\n")
        fobj.write("Zip File Created: "+str(zip_file)+"\n")
        fobj.write("-"*50+"\n")
        fobj.close()

        sender_email = "pkhanvilkar2809@gmail.com"  # Replace with your email
        app_password = "zxbrfnadzkihzkgj"  # Replace with your app password
        receiver_email = "prajaktak412@gmail.com" # Replace with the recipient's email
        subject = "Marvellous Data Shield Log and Zip File Name"
        body = "Please find the attached log file and zip file from Marvellous Data Shield System." \
        "nLog File: "+log_file_name+"\nZip File: "+str(zip_file)
        send_email(sender_email, app_password, receiver_email, subject, body, log_file_name)

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
   

def send_email_notification(log_file,zip_file):
    print("Sending email notification with log file and zip file")
    print("Log File: ",log_file)
    print("Zip File: ",zip_file)
    print("Email sent successfully")    

def restore_backup(zip_file, destination):
    border = "-" * 50
    print(border)
    print("Restore process started at", time.ctime())
    print(border)
    print("Restoring backup from zip file:", zip_file)
    print(os.path.exists(zip_file))
    # Check if zip file exists
    if not os.path.exists(zip_file):
        print("Error: Zip file does not exist.")
        return

    # Create destination directory if not exists
    os.makedirs(destination, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_file, 'r') as zobj:
            zobj.extractall(destination)

        print("Restore completed successfully!")
        print("Files extracted to:", destination)

    except zipfile.BadZipFile:
        print("Error: Invalid Zip file.")

    print(border)

def update_backup_history(zip_file, files_count):
    history_file = "backup_history.log"

    if os.path.exists(zip_file):
        zip_size = os.path.getsize(zip_file)  # in bytes
        zip_size_kb = round(zip_size / 1024, 2)
    else:
        zip_size_kb = 0

    with open(history_file, "a") as f:
        f.write(f"Date: {time.ctime()}\n")
        f.write(f"Files Copied: {files_count}\n")
        f.write(f"Zip File: {zip_file}\n")
        f.write(f"Zip Size: {zip_size_kb} KB\n")
        f.write("-" * 50 + "\n")

def display_backup_history():
    history_file = "backup_history.log"

    if not os.path.exists(history_file):
        print("No backup history found.")
        return

    print("-" * 50)
    print("--------- Backup History ---------")
    print("-" * 50)

    with open(history_file, "r") as f:
        print(f.read())

    print("-" * 50)

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
            print("4: Sends Mail with the log and zip file")
            print("5: Stores information about backup history")
            print("6: Restore backup from zip file")
            print("7: Display backup history")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory Name")
            print("TimeInterval: the time in minutes for periodic scheduling")
            print("SourceDirectory Name: Name of SourceDirectory to backedup")
            print("Optional: You can also provide a comma separated list of file extensions to exclude from backup")
            print("Example: ScriptName.py 5 Data .temp,.log,.exe")
        elif sys.argv[1] == "--history":
            display_backup_history()

        else: 
                print("Unable to proceed as there is no such option")
                print("Please use --h or --u to get more details")

    elif len(sys.argv) >= 4 and sys.argv[1] == "--restore":
            print(len(sys.argv))
            if len(sys.argv) == 4:
                zip_file = sys.argv[2]
                destination = sys.argv[3]
                restore_backup(zip_file, destination)
            else:
                print("Usage:")
                print("python script.py --restore ZipFileName DestinationFolder")

    #python3 Demo.py 5 Data
    elif len(sys.argv) >= 3 and sys.argv[1] != "--restore":
        interval = sys.argv[1]
        source = sys.argv[2]
        # Optional user exclusions
        user_exclusions = set()
        if len(sys.argv) == 4:
            user_exclusions = set(sys.argv[3].split(","))
        schedule.every(int(interval)).minutes.do(
            marvellousDataShieldStart, source, user_exclusions
        )

        print("Data Shield System Started Successfully")
        print("Excluded Extensions:", user_exclusions)
        print("Press Ctrl + C to stop execution")

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