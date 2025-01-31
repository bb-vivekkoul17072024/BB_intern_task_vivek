Task2
# AWS EC2 Instance Tag Validation Script  

## Overview  
This script retrieves all **running** EC2 instances from the specified AWS regions and checks for missing required tags. The results are saved in an **Excel file** with separate sheets for each region.  

## Functionality  
- Connects to AWS EC2 using `boto3`.  
- Fetches instance details from the specified regions (`ap-south-1`, `us-east-1`).  
- Checks if instances are **running**.  
- Validates if the required tags are present:  
  - `patch`, `ssm-key-automation`, `application_module`, `os`, `team`, `Name`  
- If any tag is missing, the instance details are recorded in an Excel sheet.  
- Saves the results in **`Sandbox_missing_tags_instances.xlsx`**.  

## Output  
Each region has a separate sheet in the Excel file, listing instances missing any of the required tags. The recorded details include:  
- `InstanceId`  
- `InstanceType`  
- `Name`  
- `application_module`  
- `team`  
- `patch`  
- `os`  
- `ssm-key-automation`  
- `State`  

## Dependencies  
- **Python**  
- **boto3** (AWS SDK for Python)  
- **openpyxl** (for handling Excel files)  

## Usage  
1. Install dependencies:  
   ```bash
   pip install boto3 openpyxl
   ```  
2. Ensure your AWS credentials are configured (`~/.aws/credentials`).  
3. Run the script:  
   ```bash
   python script.py
   ```  
4. The **`Sandbox_missing_tags_instances.xlsx`** file will be generated with the missing tag details.  

## Notes  
- The script currently checks only **running** instances.  
- You may modify the required tags list (`req_tags`) as needed.  
- The script processes instances from multiple AWS regions.  

---

This should give a clear understanding of your script for documentation purposes! 🚀
