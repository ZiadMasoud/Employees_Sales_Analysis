# Part 1: Data Cleaning and Preparation (Python)


import pandas as pd
import numpy as np

# Load the data
sales_df = pd.read_csv('sales_data.csv')
employee_df = pd.read_csv('employee_data.csv')

"""#  Clean Sales Data:"""

# Convert `SalesAmount` to numeric after removing symbols and commas.
sales_df['SalesAmount'] = sales_df['SalesAmount'].replace('[\$,]', '', regex=True).astype(float)
sales_df['SalesAmount'] = pd.to_numeric(sales_df['SalesAmount'], errors='coerce')
print(sales_df)

# Standardize `PurchaseDate` to pandas `datetime`.
sales_df['PurchaseDate'] = pd.to_datetime(sales_df['PurchaseDate'], errors='coerce', dayfirst=True)
sales_df

# Handle missing or invalid data by replacing them with appropriate defaults (e.g., `NaN` for missing data).
sales_df.fillna(0 ,inplace=True)
sales_df

"""# Clean Employee Data:

"""

employee_df

# Convert `Salary` to numeric after removing symbols and commas.
employee_df['Salary'] = employee_df['Salary'].replace('[\$,]', '', regex=True).astype(float)
employee_df

employee_df['Salary'] = pd.to_numeric(employee_df['Salary'], errors='coerce')
employee_df.dtypes

# Replace inconsistent `EmployeeID` or `SupervisorID` with clean integers.
employee_df['SupervisorID'] = pd.to_numeric(employee_df['SupervisorID'], errors='coerce')
employee_df

# Handle any missing `SupervisorID` values by filling them with `NaN`
employee_df['SupervisorID'].replace(np.nan, 0, inplace=True)

employee_df['SupervisorID'] = employee_df['SupervisorID'].astype('Int64')

employee_df

# Save cleaned data
sales_df.to_csv('cleaned_sales.csv', index=False)
employee_df.to_csv('cleaned_employees.csv', index=False)