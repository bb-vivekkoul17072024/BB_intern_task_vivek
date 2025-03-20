AWS Multi-Account Cost Report Generator

Overview

This Python script retrieves AWS cost data for multiple linked accounts under an AWS Organization using AWS Cost Explorer and Organizations APIs.
It then generates an Excel report summarizing monthly costs, identifying significant changes, and providing a breakdown of service costs when a significant
increase is detected.

Features

Fetches all active linked AWS accounts under the organization.

Retrieves the last 6 months of cost data for each account using AWS Cost Explorer.

Generates an Excel report summarizing:

Monthly costs for each account.

Cost changes from the previous month.

Percentage change in cost.

A separate breakdown of service costs if the increase exceeds 50%.

Highlights cost changes using color coding:

Yellow: Cost increased from the previous month.

Green: Cost decreased from the previous month.

Orange: Cost increased by 50% or more.

Red: Cost increased by 100% or more.

Prerequisites

1. AWS Credentials

Ensure you have AWS credentials configured to allow access to Organizations and Cost Explorer APIs.

You can configure credentials using the AWS CLI:

The script assumes that the IAM role or user has the following permissions:

2. Install Dependencies

Ensure you have Python installed along with the required dependencies:

Usage

Run the script using:

This will:

Fetch all linked AWS accounts.

Retrieve cost data for the last 6 months.

Generate an Excel report named aws_multi_account_costs_YYYYMMDD.xlsx.

Output

The generated Excel file contains:

Main Report Sheet: Monthly cost summary per account.

Service Breakdown Sheets: Detailed cost breakdown per service (only for accounts where cost increased by 50% or more).

File Structure

Future Improvements

Add support for additional cost metrics.

Store historical data in a database.

Generate automated alerts for high cost spikes.
