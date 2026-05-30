import os

def main():
    print("PID of running process is:", os.getpid())   
    print("PID of parent process id:", os.getppid())

if __name__ == "__main__":
    main()