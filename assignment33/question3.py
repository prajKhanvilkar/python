import psutil
import operator
import sys
import time

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

def write_memory_usage_to_file(file_object):
    border = "-"*50
    file_object.write(border+"\n")
    file_object.write("This log File is created by Marvellous Automation"+"\n")
    file_object.write("This is Open File Monitoring Feature"+"\n")
    file_object.write(border+"\n")

    file_object.write("-----------------Process Scan Report---------------"+"\n")
    file_object.write(border+"\n")

    top_processes = get_top_memory_processes(10)
    file_object.write(f"{'PID':<10} | {'Name':<25} | {'RSS (MB)':<15} | {'VMS (MB)':<15} | {'Mem %':<8}\n")
    file_object.write("-" * 80 + "\n")

    for proc in top_processes:
        rss_mb = format_bytes(proc['rss'])
        vms_mb = format_bytes(proc['vms'])
        mem_percent = f"{proc['mem_percent']:.2f}%"
        file_object.write(f"{proc['pid']:<10} | {proc['name']:<25} | {rss_mb:<15} | {vms_mb:<15} | {mem_percent:<8}\n")
    file_object.write(border+"\n")
    file_object.write("--------------- Report Completed------------------"+"\n")
    file_object.write(border+"\n")
# Example of how to use this with a file object (e.g., a physical file or standard output)
if __name__ == "__main__":
    # Option 1: Write to a physical file
    timeStamp = time.strftime("%Y_%M_%d_%H_%M_%S")
    fileName = "MarvellousAssignment3%s.log"%timeStamp
    with open(fileName, "w") as f:
        write_memory_usage_to_file(f)
    print("Memory usage report written to memory_usage.txt")

    # Option 2: Write to standard output (console) as a file object
    print("\n--- Top 10 Memory Consuming Processes (Console Output) ---")
    write_memory_usage_to_file(sys.stdout)

