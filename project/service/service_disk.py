import psutil 

def get_check_disk():
    """
    this api use Check CPU Percent and High CPU Alert, Check Memory Space And High Memory Use Alart, Your Disk Alert and Percent

    """
    Threshold_CPU = 10
    Threshold_Memory = 50
    Threshold_disk = 30 
    Current_CPU = psutil.cpu_percent(interval=1)
    Current_Memory = psutil.virtual_memory().percent
    Current_Disk =  psutil.disk_usage('/').percent
    disk_alert = (f"Disk Percent {Current_Disk} is Very High 😡😡 for your Threshold {Threshold_disk} " if Current_Disk > Threshold_disk else "Disk memory Normal..", Current_Disk)
    memory_alert = (f"Memory Percent is Very high" if Current_Memory > Threshold_Memory else "Memory is Normal..", Current_Memory)
    status = (f"Current CPU {Current_CPU}  Very High 😡😡 for your Threshold {Threshold_CPU}" if  Current_CPU > Threshold_CPU else "CPU HEALTHY...", Current_CPU)
    print("-"*30)
    return{
        "CPU Percent" : status,
        "Current memory " : memory_alert,
        "Disk Percent" : disk_alert,

    }