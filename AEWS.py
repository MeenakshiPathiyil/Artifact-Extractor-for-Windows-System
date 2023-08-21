import psutil
import pandas as pd

# Function to retrieve detailed information about a process given its PID
def get_process_info(pid):
    try:
        # Get process object using PID
        process = psutil.Process(pid)
        # Extract specific attributes of the process
        info = process.as_dict(attrs=['pid', 'name', 'ppid'])

        # Fetch the parent process info
        parent_pid = info['ppid']
        parent_process = psutil.Process(parent_pid)
        parent_info = parent_process.as_dict(attrs=['name'])

        # Add parent process name to the info dictionary
        info['parent_name'] = parent_info['name']

        return info
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return None

# Function to retrieve information about currently running processes
def get_running_processes():
    process_list = []
    for proc in psutil.process_iter(['pid']):
        try:
            # Get process info for each running process
            process_info = get_process_info(proc.info['pid'])
            if process_info:
                process_list.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_list

# Get information about running processes
process_data = get_running_processes()
df = pd.DataFrame(process_data)

# Function to retrieve information about Windows services
def get_services_as_dict():
    service_dict = {}
    for service in psutil.win_service_iter():
        # Extract specific attributes of the service
        service_info = {
            "name": service.name(),
            "display_name": service.display_name(),
            "status": service.status()
        }
        service_dict[service.pid()] = service_info
    return service_dict

# Get information about Windows services
services = get_services_as_dict()
df2 = pd.DataFrame(services)


# Get information about system memory usage
memory = psutil.virtual_memory()
memory_used_gb = memory.used / (1024 ** 3)
total_memory_gb = memory.total / (1024 ** 3)
available_memory_gb = memory.available / (1024 ** 3)
memory_perc = memory.percent

# Get information about logged-in users
user = psutil.users()
df3 = pd.DataFrame(user)

# Get information about disk usage
usage_disk = psutil.disk_usage('/')
total_gb = usage_disk.total / (1024 ** 3)
used_gb = usage_disk.used / (1024 ** 3)
free_gb = usage_disk.free / (1024 ** 3)
disk_perc = usage_disk.percent

# Write process data to CSV files
df.to_csv('processes.csv', index=False)

# Write services data to CSV files
df2.to_csv('services.csv', index=False)

# Write user data to CSV files
df3.to_csv('users.csv', index=False)

# Write system information to a text file
with open('sys_info.txt', 'w') as f:
    f.write('Total space in disk = ' + str(total_gb) + '\n')
    f.write('Used space in disk = ' + str(used_gb) + '\n')
    f.write('Free space in disk = ' + str(free_gb) + '\n')
    f.write('Disk Usage Percent = ' + str(disk_perc) + '\n')
    f.write('Total Memory = ' + str(total_memory_gb) + '\n')
    f.write('Memory used = ' + str(memory_used_gb) + '\n')
    f.write('Available Memory = ' + str(available_memory_gb) + '\n')
    f.write('Memory Percent = ' + str(memory_perc))