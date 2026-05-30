#Command Line
import psutil
import sys

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
        print("Inside projects logic")
        print("Time Interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])

    else:
        print("Invalid Number of Command Line Arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

            
    print(border)
    print("---------Thank you fro using our script-----------")
    print(border)

if __name__ =="__main__":
    main()