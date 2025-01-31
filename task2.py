from datetime import datetime, timedelta, timezone
import boto3
from openpyxl import Workbook

regions = {"ap-south-1", "us-east-1"}
req_tags = {'patch', 'ssm-key-automation', 'application_module', 'os', 'team', 'Name'}

workbook = Workbook()
workbook.remove(workbook.active)  # Remove the default sheet

for region in regions:
    sheet = workbook.create_sheet(title=region)
    sheet.append(['InstanceId', 'InstanceType', 'Name', 'application_module', 'team', 'patch', 'os', 'ssm', 'State'])

    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    
    for res in response['Reservations']:
        for instance in res['Instances']:
            launch_time = instance['LaunchTime']
            curr = datetime.now(timezone.utc)
            running = curr - launch_time  
            if instance['State']['Name']=='running':
                # if running > timedelta(hours=6):
                    instance_tags_dict = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                    missing_tags = req_tags - set(instance_tags_dict.keys())
                    
                    if missing_tags:
                        sheet.append([
                            instance['InstanceId'],
                            instance['InstanceType'],
                            instance_tags_dict.get('Name', 'No name'),
                            instance_tags_dict.get('application_module', '.'),
                            instance_tags_dict.get('team', '.'),
                            instance_tags_dict.get('patch', '.'),
                            instance_tags_dict.get('os', '.'),
                            instance_tags_dict.get('ssm-key-automation'),
                            instance['State']['Name']
                        ])

workbook.save('Sandbox_missing_tags_instances.xlsx')
print("Done")