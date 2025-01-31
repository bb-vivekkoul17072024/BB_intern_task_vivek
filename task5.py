import boto3

# Initialize EC2 client for ap-south-1 (Mumbai region)
ec2_ap_south_1 = boto3.client('ec2', region_name="ap-south-1")

# Create a Security Group without specifying VPCId (it will use the default VPC)
response = ec2_ap_south_1.create_security_group(
    GroupName='vivek_sg',
    Description='Security group for EC2 instance'
)

security_group_id = response['GroupId']
print(f"Security Group Created with ID: {security_group_id}")

# Add Inbound Rules (SSH & HTTP)
ec2_ap_south_1.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # SSH for all (change this in production)
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # HTTP for all
        },
    ]
)
print(f"Inbound rules added to Security Group {security_group_id}")

# Create an EC2 instance (it will be created in the default VPC)
instances = ec2_ap_south_1.run_instances(
    ImageId='ami-00bb6a80f01f03502',  # Replace with your valid AMI ID
    InstanceType='t3.micro',
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=[security_group_id], 
    KeyName='my_keypair_code',  # Replace with your key pair name
    TagSpecifications=[  # Adding tags to the instance
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'vivek'},
                {'Key': 'environment', 'Value': 'Dev'},
                {'Key': 'team', 'Value': 'Cloudnauts'},
                {'Key': 'owner', 'Value': 'vivek.koul@bigbasket.com'},
                {'Key': 'creation-mode', 'Value': 'boto3'}
            ]
        }
    ]
)

# Extract instance details
for instance in instances['Instances']:
    print(f"Instance {instance['InstanceId']} created with Security Group {security_group_id}")
