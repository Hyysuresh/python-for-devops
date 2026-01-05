import boto3
s3 = boto3.client('s3')
def get_s3_bucket():
    response = s3.list_buckets()['Buckets']
    for bucket in response:
        bucket_name = bucket['Name']
        return{bucket_name}
    




    