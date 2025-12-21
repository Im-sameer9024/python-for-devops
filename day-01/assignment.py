import psutil

#-------------- first python script -----------
# name = input("Enter your name : ")
# marks = int(input("Enter your marks : "))

# while  marks <= 100 :
#     if marks >= 90 :
#         print(f"{name} is Got Grade A")
#         break
#     elif marks >= 80 :
#         print(f"{name} is Got Grade B")
#         break
#     elif marks >= 70 :
#         print(f"{name} is Got Grade C")
#         break
#     elif marks >= 60  :
#         print(f"{name} is Got Grade D")
#     else :
#         print("Participate in the exam again ")
        


# You will create a Python script that:
# - Takes threshold values (CPU, disk, memory) from **user input**
# - Also fetches system metrics using a Python library (example: `psutil`)
# - Compares metrics against thresholds
# - Prints the result to the **terminal**

cpu = int(input("Enter the cpu threshold : "))
disk = int(input("Enter the disk threshold : "))
memory = int(input("Enter the memory threshold : "))

def compare_user_system(cpu, disk, memory):
        if cpu > psutil.cpu_percent():
            print(f"cpu is not overloaded : {psutil.cpu_percent()}")
        else:
            print(f"cpu is overloaded  : {psutil.cpu_percent()} ")
            
            
        if disk > psutil.disk_usage('/').percent:
            print(f"disk is not overloaded : {psutil.disk_usage('/').percent}")
        else: 
            print(f"disk is overloaded : {psutil.disk_usage('/').percent}")
            
        if memory > psutil.virtual_memory().percent:
            print(f"memory is not overloaded : {psutil.virtual_memory().percent}")
        else: 
            print(f"memory is overloaded : {psutil.virtual_memory().percent}")
    
compare_user_system(cpu, disk, memory)


    