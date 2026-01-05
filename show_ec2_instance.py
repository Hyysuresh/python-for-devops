#----------------------------------- SHOW EC2 Instance --------------------------
import boto3

ec2 = boto3.client('ec2', region_name='eu-north-1')

response = ec2.describe_instances(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
)
def show_instance():
    for Reservation in response["Reservations"]:
        for instace in Reservation['Instances']:
            print(f"{instace['InstanceId']}, PublicIp: {instace['PublicIpAddress']}, PublicDNS: {instace['PublicDnsName']} ")
            
show_instance()
#-------------------------------------------------------------------------------------
