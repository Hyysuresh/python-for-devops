
#-------------------------------- Use Class Fuction -----------------------------
import boto3
class AWSUTILITY:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.ec2 = boto3.client('ec2', region_name='eu-north-1')
    def create_bucket(self, bucket_name):
        try:
            response = self.s3.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'eu-north-1',
            })
            if response['ResponseMetadata']["HTTPStatusCode"] == 200:
                print('bucket Create Successfully')
            else:
                print('Error occured is not create')
        except:
            print('occured Error')
    def show_bucket(self):
        response = self.s3.list_buckets()
        for bucket in response['Buckets']:
            print(bucket['Name'])
    def show_ec2_instance(self):
        respons = self.ec2.describe_instances()
        for Reservation in respons['Reservations']:
            for instance in Reservation['Instances']:
                print("Instance ID :", instance['InstanceId'])
                print("State       :", instance['State']['Name'])
                print("InstanceType:", instance['InstanceType'])
                print("-" * 30)
        

        
if __name__ == "__main__":
    slow = AWSUTILITY()
    slow.create_bucket("mama-bhanja-ki-ladai3")
    slow.show_bucket()
    slow.show_ec2_instance()

#------------------------------------------------ And Class Fuction -----------------------------


 