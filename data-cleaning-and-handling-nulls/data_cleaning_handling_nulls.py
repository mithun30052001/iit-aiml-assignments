import pandas as pd
import numpy as np

data = {
    'patient_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 101, 107, 118, 119, 120],
    'age': ['25', '34', None, '45', '29', None, '38', '52', '27', '41',
            '33', 'unknown', '48', '26', '35', '25', '38', '31', None, '44'],
    'weight': ['70', '65', '80', None, '75', None, '68', '90', '72', '85',
               '78', None, '82', '69', 'N/A', '70', '68', '74', None, '88'],
    'blood_pressure': [120, 130, None, 140, 125, None, 135, None, 118, 145,
                      128, None, 138, 122, None, 120, 135, 126, None, 142],
    'medication': ['Aspirin', 'Metformin', 'Lisinopril', None, 'Aspirin',
                   'Metformin', 'Lisinopril', 'Aspirin', None, 'Metformin',
                   'Lisinopril', 'Aspirin', None, 'Metformin', 'Aspirin',
                   'Aspirin', 'Lisinopril', 'Metformin', 'Aspirin', None],
    'insurance_provider': ['Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None,
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', 'Blue Cross',
                          'Aetna', None, 'UnitedHealth', 'Blue Cross', 'Aetna',
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None]
}

df = pd.DataFrame(data)

#Task 1 Inspect the Data

print(f"Info about data frames: {df.info()}")
print(f"Count of missing values per column: {df.isnull().sum()}")
print(f"Percentage of missing values : {(df.isnull().sum() / len(df)) * 100}")
print(f"Count of duplicated rows: {df.duplicated().sum()}")

#Task 2: Data Type Conversion

df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
print(f"Dataframe after age and weight conversion: {df}")

age_missing = df['age'].isna().sum()
weight_missing = df['weight'].isna().sum()

print("Missing values in age:", age_missing)
print("Missing values in weight:", weight_missing)

df['insurance_provider'] = df['insurance_provider'].astype('category')
print(f"verifying data types after conversion: {df.dtypes}")

#Task 3: Handle Missing Values

df['age'].fillna(df['age'].median())
df['weight'].fillna(df['weight'].median())
df['blood_pressure'].fillna(df['blood_pressure'].median())
df['medication'].fillna(df['medication'].mode()[0])
df['insurance_provider'] = df['insurance_provider'].cat.add_categories('Unknown')
df['insurance_provider'].fillna('Unknown')
print("===================")
print(f"Verifying no missing values remain: {df.isnull().sum()}")
print("===================")

#Task 4: Handle Duplicates
print(f"Duplicate rows: {df[df.duplicated(keep=False)]}")
print(f"Duplicate patient_id rows: {df[df.duplicated(subset=['patient_id'], keep=False)]}")
print(f"Shape before removing duplicates: {df.shape}")
df_duplicate_drop = df.drop_duplicates(subset=['patient_id'], keep='first')
print(f"Shape after removing duplicates:{df_duplicate_drop.shape}")

#Task 5: Complete Workflow with Verification

df = pd.DataFrame(data) # Reload dataframe
df_clean = df.copy() # Create a copy for cleaning

shape_before = df_clean.shape
missing_before = df_clean.isnull().sum()
duplicates_before = df_clean.duplicated(subset=['patient_id']).sum()
dtypes_before = df_clean.dtypes

df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce')
df_clean['weight'] = pd.to_numeric(df_clean['weight'], errors='coerce')

df_clean['age'].fillna(df_clean['age'].median())
df_clean['weight'].fillna(df_clean['weight'].median())
df_clean['blood_pressure'].fillna(df_clean['blood_pressure'].median())

df_clean['medication'].fillna(df_clean['medication'].mode()[0])

df_clean['insurance_provider'].fillna('Unknown')
df_clean['insurance_provider'] = df_clean['insurance_provider'].astype('category')

df_clean = df_clean.drop_duplicates(subset=['patient_id'], keep='first')

shape_after = df_clean.shape
missing_after = df_clean.isnull().sum()
duplicates_after = df_clean.duplicated(subset=['patient_id']).sum()
dtypes_after = df_clean.dtypes

print("\n========== DATA CLEANING REPORT ==========\n")

print("Shape Before Cleaning:", shape_before)
print("Shape After Cleaning :", shape_after)

print("\nMissing Values Before:\n", missing_before)
print("\nMissing Values After:\n", missing_after)

print("\nDuplicates Before:", duplicates_before)
print("Duplicates After :", duplicates_after)

print("\nData Types Before:\n", dtypes_before)
print("\nData Types After:\n", dtypes_after)

print("\n==========================================")