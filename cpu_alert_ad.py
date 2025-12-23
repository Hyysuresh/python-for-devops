import psutil 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#  -----------configurastion------------------
CPU_THRESHOLD = 20
SERDER_EMAIL= "noreply@gmail.com" # google manage email
RECEIVER_EMAIL = "@gmail.com" # Email address to which the email is to be sent
PASSWORD = "vqsd tagh tkyi durhsh" #google manage → my password → create app 
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

def Check_CPU_Threshold():
    current_cpu = psutil.cpu_percent(interval=1)
    print("current cpu percent :", current_cpu)
    if current_cpu > CPU_THRESHOLD:
        print("CPU is threshold sent to email ..")
        msg = MIMEMultipart()
        msg['FROM'] = SERDER_EMAIL
        msg['TO'] = RECEIVER_EMAIL
        msg['SUBJECT'] = f"Alert: CPU Usage : {current_cpu}%"
        body = f"Hello Your Current CPU {current_cpu} is Very high 😡😡 for Your Threshold {CPU_THRESHOLD} please check your termainal"
        msg.attach(MIMEMultipart(body, 'plain'))
        try:
            server = smtplib.SMTP(SMTP_SERVER, PORT)
            server.starttls()
            server.login(SERDER_EMAIL, PASSWORD)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("CPU is normal ...")
Check_CPU_Threshold()

