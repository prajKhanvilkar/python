import time
import schedule
import datetime

def fun(): 
    print("Inside fun at:", datetime.datetime.now())

def main():
    print("Inside Marvellous AutiomationScript", datetime.datetime.now())
    schedule.every(20).seconds.do(fun)
#problem

if __name__ == "__main__":
    main()