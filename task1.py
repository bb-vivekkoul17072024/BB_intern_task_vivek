import boto3
import csv
from openpyxl import Workbook

ec2_ap_south_1 = boto3.client('ec2', region_name="ap-south-1")
ec2_us_east_1 = boto3.client('ec2', region_name="us-east-1")

response_ap_south_1 = ec2_ap_south_1.describe_volumes()
response_us_east_1 = ec2_us_east_1.describe_volumes()

workbook = Workbook()

sheet_ap_south_1 = workbook.active
sheet_ap_south_1.title = 'ap-south-1'
sheet_ap_south_1.append(['Volume Type', 'Volume Id', 'Name', 'Size', 'State'])

for volume in response_ap_south_1['Volumes']:
    name = ''
    if 'Tags' in volume:
        for tag in volume['Tags']:
            if tag['Key'] == 'Name':
                name = tag['Value']
                break
    if volume['State'] == 'available':
        sheet_ap_south_1.append([volume['VolumeType'], volume['VolumeId'], name, volume['Size'], volume['State']])

sheet_us_east_1 = workbook.create_sheet(title='us-east-1')
sheet_us_east_1.append(['Volume Type', 'Volume Id', 'Name', 'Size', 'State'])

for volume in response_us_east_1['Volumes']:
    name = ''
    if 'Tags' in volume:
        for tag in volume['Tags']:
            if tag['Key'] == 'Name':
                name = tag['Value']
                break
    if volume['State'] == 'available':
        sheet_us_east_1.append([volume['VolumeType'], volume['VolumeId'], name, volume['Size'], volume['State']])

workbook.save("available_volumes_sandbox.xlsx")