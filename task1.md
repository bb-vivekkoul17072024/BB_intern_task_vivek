Task1: 

- **Purpose:** This script retrieves and lists all **available** EBS volumes from two AWS regions: `ap-south-1` and `us-east-1`.  
- **Functionality:**  
  - Connects to AWS EC2 using `boto3`.  
  - Fetches volume details for the specified regions.  
  - Extracts relevant information: **Volume Type, Volume ID, Name (if available), Size, and State**.  
  - Filters only **available** volumes.  
  - Saves the data in an Excel file with separate sheets for each region.  
- **Output File:** `available_volumes_sandbox.xlsx`.  
- **Dependencies:** Python, `boto3`, `openpyxl`.
