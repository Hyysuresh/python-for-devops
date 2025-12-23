import psutil
import smtplib

def Check_CPU_THRESHOLD():
    input_cpu = int(input("Enter the CPU Percent: " ))
    current_cpu = psutil.cpu_percent(interval=1)
    print("the Percent CPU is", current_cpu)

    if current_cpu > input_cpu:
        print("CPU is THRESHOLD sent to email ...")
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("your_email", "password")
        message = "Message_you_need_to_send"
        s.sendmail("your_email", "receiver_email", f"Alert your cpu is very high {current_cpu}" )
        s.quit()
        print("mail send successfully")
    else:
        print("CPU is Normal...")
Check_CPU_THRESHOLD()