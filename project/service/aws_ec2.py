import boto3

def ec2_instance_show():
    ec2 = boto3.client('ec2', region_name='eu-north-1')
    reponse = ec2.describe_instances()['Reservations']
    for Reservation in reponse:
        for instance in Reservation['Instances']:
            instance_name = instance['InstanceId']
            return{
                instance_name
            }
            