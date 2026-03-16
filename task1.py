# Import libraries
import pandas as pd

# 1. Load Dataset
df = pd.read_excel("Online Retail.xlsx")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 2. Data Quality Assessment

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check negative values
print("\nNegative Quantity Records:")
print(df[df['Quantity'] < 0].shape)

print("\nNegative UnitPrice Records:")
print(df[df['UnitPrice'] <= 0].shape)

# 3. Data Cleaning

# Remove rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove duplicate rows
df = df.drop_duplicates()

# Remove invalid values
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Convert InvoiceDate to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 4. Feature Engineering

# Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Extract Year and Month
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month

# 5. Final Dataset Information
print("\nCleaned Dataset Info:")
print(df.info())

# 6. Save Clean Dataset
df.to_csv("cleaned_online_retail.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as cleaned_online_retail.csv")