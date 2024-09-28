import pandas as pd

# Load the raw data
file_path = '../../data/raw_data/student_performance.csv'  # Update with your actual file path
df = pd.read_csv(file_path)

# Display the first few rows to understand the data structure
print("Initial Data Preview:")
print(df.head())

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Example: Fill missing values or drop rows/columns if necessary
# Here, I'll just drop rows with any missing values as an example
df_cleaned = df.dropna()

# If you need to convert categorical data to numeric (example: gender 'M' -> 0, 'F' -> 1)
# df_cleaned['gender'] = df_cleaned['gender'].map({'M': 0, 'F': 1})

# Save the cleaned data to the processed_data folder
processed_file_path = '../../data/processed_data/student_performance_cleaned.csv'
df_cleaned.to_csv(processed_file_path, index=False)

print("Preprocessing complete. Cleaned data saved to:", processed_file_path)
