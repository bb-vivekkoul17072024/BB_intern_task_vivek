Task5:
# AWS EC2 Instance Creation with Security Group  

## Overview  
This script automates the creation of an EC2 instance with a custom security group using **AWS Boto3 SDK**. It performs the following tasks:
1. Creates a **Security Group** with SSH and HTTP inbound rules.
2. Creates an EC2 instance in the default VPC and associates the security group.
3. Tags the EC2 instance with useful metadata (like `Name`, `environment`, `team`, etc.).

## Functionality  
- **Creates a Security Group** with SSH (port 22) and HTTP (port 80) open to all IP addresses (adjustable in production environments).  
- **Creates an EC2 instance** using a specified AMI in the `ap-south-1` region (Mumbai).  
- **Assigns the created Security Group** to the EC2 instance.  
- **Tags the EC2 instance** with various metadata, including the instance's owner, environment, and creation method.  

## Input  
- **AWS credentials** (configured using `boto3`).
- **AMI ID**: The AMI ID for the EC2 instance (replace `'ami-00bb6a80f01f03502'` with a valid one).
- **Key Pair**: The name of the EC2 key pair for SSH access (`'my_keypair_code'`).

## Output  
- The script outputs the **Security Group ID** and **EC2 instance ID** to the console.  
- **Security Group**: Created with SSH and HTTP inbound rules.
- **EC2 Instance**: Created in the default VPC with the specified security group and tags.

## Dependencies  
- **Python**  
- **boto3** (AWS SDK for Python)  

## Usage  
1. Install the required dependencies:  
   ```bash
   pip install boto3
   ```  
2. Ensure that AWS credentials are configured on your machine (`~/.aws/credentials` or via environment variables).  
3. Replace the placeholder values in the script:  
   - Update the AMI ID (`'ami-00bb6a80f01f03502'`) with a valid one for your region.  
   - Use your own EC2 key pair name (`'my_keypair_code'`).  
4. Run the script:  
   ```bash
   python create_ec2_instance.py
   ```  
5. Check the console output for details about the created EC2 instance and Security Group.

## Notes  
- The script creates resources in the **default VPC** of the selected region (`ap-south-1`).  
- It is highly recommended to limit SSH access in production environments to trusted IPs instead of allowing open access (`'0.0.0.0/0'`).  
- The created EC2 instance is **tagged** with details such as `Name`, `team`, and `owner`.  

---

This README file explains how the script works and provides guidance on how to configure and run it. You can add it to your repository to help others understand the script's functionality.
