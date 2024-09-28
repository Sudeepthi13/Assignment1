import pandas as pd

# Load the raw data
file_path = '../../data/raw_data/frailty_data.csv'  # Adjusted file path to point to the raw_data folder
df = pd.read_csv(file_path)

# Display the data to check if it's loaded correctly
print(df.head())

# Check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Example: If no cleaning is needed, you can just save it directly to processed_data
# Otherwise, you can apply any data cleaning steps here

# Save the cleaned data
cleaned_file_path = '../../data/processed_data/cleaned_frailty_data.csv'  # Save cleaned data
df.to_csv(cleaned_file_path, index=False)

print("Cleaned data saved successfully.")
