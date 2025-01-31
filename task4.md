Task4:

# AWS Unlinked Snapshots Report  

## Overview  
This script generates a report of **unlinked snapshots** across multiple AWS EC2 regions. It compares snapshots with AMIs and lists snapshots that are **not associated with any AMI** (unlinked snapshots). The results are saved into an **Excel file** for each region.  

## Functionality  
- **Fetches snapshots and AMIs** in multiple AWS regions.  
- **Identifies snapshots that are not associated with any AMI**.  
- **Sorts the unlinked snapshots** by their start time.  
- **Generates an Excel report** with unlinked snapshot details.  

## Input  
- **AWS credentials** (configured using `boto3`).
- **Regions**: `ap-south-1`, `us-east-1`.

## Output  
- An **Excel file** (`unlinked_snapshots_by_region.xlsx`) that contains sheets for each region with the following columns:  
  - `Snapshot Id`
  - `Volume Id`
  - `Size (GiB)`
  - `Start time`

## Dependencies  
- **Python**  
- **boto3** (AWS SDK for Python)  
- **openpyxl** (for generating Excel files)  

## Usage  
1. Install the required dependencies:  
   ```bash
   pip install boto3 openpyxl
   ```  
2. Ensure AWS credentials are configured on your machine (`~/.aws/credentials`).  
3. Run the script:  
   ```bash
   python script.py
   ```  
4. Check the generated `unlinked_snapshots_by_region.xlsx` for a detailed report.  

## Notes  
- The script identifies **unlinked snapshots** that are not associated with any AMI.  
- The report is sorted by **snapshot start time** (from the oldest to the newest).  
- Each region will have its own sheet in the Excel file.  
- **Unlinked snapshots** are defined as snapshots that do not appear in any AMI's block device mapping.

---
