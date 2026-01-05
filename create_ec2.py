#------------------------ Create AWS EC2 Instance------------------------
instaces = ec2.create_instances(
    BlockDeviceMappings=[
        {
            'Ebs': {
                'VolumeSize': 20,
                'VolumeType': 'gp3'
            },
            'DeviceName': '/dev/sdf'
        },
    ],
    ImageId = 'ami-0fa91bc90632c73c9',
    InstanceType = 't3.micro',
    KeyName = 'ali-baba-key',
    MinCount = 1,
    MaxCount = 1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'python-for-devops3'}]
        },
    ]

)
instance = instances[0]
print(instance.id)


instance.wait_until_running()

instance.reload()

print("Public DNS:", instance.public_dns_name)
print("Public IP:", instance.public_ip_address)
#-----------------------------------------------------------------------------