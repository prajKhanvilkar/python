import sys
def main():
    Border = "-" * 40
    print(Border)
    print("--------Marvellous Automation-----------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform ____")
            print("This is a automation script")
        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument 1: ________")
            print("Argument 2: ________")
        else:
            print("Use the given flag as :")
            print("For Help : --h or --H")
            print("For Usage : --u or --U")
    else:
        print("Invalid number of arguments")
        print("Use the given flag as :")
        print("For Help : --h or --H")
        print("For Usage : --u or --U")
    print(Border)
    print("------Thank you for using our script----")
    print("--------Marvellous Infosystems----------")
    print(Border)

if __name__ == "__main__":
    main()