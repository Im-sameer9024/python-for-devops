import psutil

def get_cpu_usage():
    cpu_threshold = float(input("Enter CPU usage threshold (%): "))
    memory_threshold = float(input("Enter Memory usage threshold (%): "))
    disk_threshold = float(input("Enter Disk usage threshold (%): "))

    cpu_use = psutil.cpu_percent(interval=1)
    memory_use = psutil.virtual_memory().percent
    disk_use = psutil.disk_usage('/').percent
    
    # compare CPU 

    if cpu_use > cpu_threshold:
        print(f"⚠️ CPU usage is above threshold! Current usage: {cpu_use}% user Input threshold: {cpu_threshold}%")
    else:
        print(f"✅ CPU usage is within acceptable limits. Current usage: {cpu_use}% user Input threshold: {cpu_threshold}%")

    # compare Memory

    if memory_use > memory_threshold:
        print(f"⚠️ Memory usage is above threshold! Current usage: {memory_use}% user Input threshold: {memory_threshold}%")
    else:
        print(f"✅ Memory usage is within acceptable limits. Current usage: {memory_use}% user Input threshold: {memory_threshold}%")

    # compare Disk

    if disk_use > disk_threshold:
        print(f"⚠️ Disk usage is above threshold! Current usage: {disk_use}% user Input threshold: {disk_threshold}%")
    else:
        print(f"✅ Disk usage is within acceptable limits. Current usage: {disk_use}% user Input threshold: {disk_threshold}%")

get_cpu_usage()