Task3

# AWS EC2 Missing Tags Updater  

## Overview  
This script reads an **Excel file (`missing_tags_instances.xlsx`)** containing EC2 instance details and updates missing or empty tags for **running** instances in AWS.  

## Functionality  
- **Loads input data** from an Excel file.  
- **Validates instance IDs** using a regex pattern.  
- **Fetches EC2 instances** from AWS for the specified regions (`ap-south-1`, `us-east-1`).  
- **Checks for missing or empty tags** based on the input file.  
- **Updates tags** for running instances where necessary.  

## Input  
- **Excel File:** `missing_tags_instances.xlsx`  
- **Columns in Excel:**  
  - `InstanceId`  
  - `InstanceType`  
  - `Name`  
  - `application_module`  
  - `team`  
  - `patch`  
  - `os`  
  - `ssm`  
  - `State`  

## Output  
- The script **validates and updates missing tags** on running EC2 instances.  
- Prints messages for successful updates or errors.  

## Dependencies  
- **Python**  
- **boto3** (AWS SDK for Python)  
- **openpyxl** (for reading Excel files)  

## Usage  
1. Install dependencies:  
   ```bash
   pip install boto3 openpyxl
   ```  
2. Ensure AWS credentials are configured (`~/.aws/credentials`).  
3. Place `missing_tags_instances.xlsx` in the script directory.  
4. Run the script:  
   ```bash
   python script.py
   ```  
5. Check the console for tag update logs.  

## Notes  
- The script only processes **running** instances.  
- It updates only **missing or empty tags** based on the Excel file.  
- If an instance ID in the Excel file is invalid, it is ignored.  

---

