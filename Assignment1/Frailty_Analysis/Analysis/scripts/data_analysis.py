import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
cleaned_file_path = '../../data/processed_data/cleaned_frailty_data.csv'  # Adjust path as needed
df = pd.read_csv(cleaned_file_path)

# Display the first few rows of the dataframe
print(df.head())

# Convert the 'Frailty' column to numeric
df['Frailty'] = df['Frailty'].map({'N': 0, 'Y': 1})

# Summary statistics
summary_stats = df.describe()
print("Summary Statistics:\n", summary_stats)

# Check for correlations (now includes Frailty as numeric)
correlation_matrix = df.corr()
print("Correlation Matrix:\n", correlation_matrix)

# Visualization 1: Grip Strength vs Age
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Age', y='Grip_strength', hue='Frailty')
plt.title('Grip Strength vs Age')
plt.xlabel('Age (years)')
plt.ylabel('Grip Strength (kg)')
plt.savefig('../../reports/figures/grip_strength_vs_age.png')  # Save the figure
plt.show()

# Visualization 2: Distribution of Grip Strength
plt.figure(figsize=(8, 6))
sns.histplot(df['Grip_strength'], bins=10, kde=True)
plt.title('Distribution of Grip Strength')
plt.xlabel('Grip Strength (kg)')
plt.ylabel('Frequency')
plt.savefig('../../reports/figures/distribution_of_grip_strength.png')  # Save the figure
plt.show()

# Visualization 3: Boxplot of Grip Strength by Frailty Status
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Frailty', y='Grip_strength')
plt.title('Grip Strength by Frailty Status')
plt.xlabel('Frailty')
plt.ylabel('Grip Strength (kg)')
plt.savefig('../../reports/figures/grip_strength_by_frailty.png')  # Save the figure
plt.show()

# Save summary statistics to a CSV file
summary_stats.to_csv('../../analysis/results/summary_statistics.csv')
