import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
file_path = '../../data/processed_data/student_performance_cleaned.csv'
df = pd.read_csv(file_path)

# 1. Distribution of Math Scores
plt.figure(figsize=(8, 6))
sns.histplot(df['math score'], bins=20, kde=True)
plt.title('Distribution of Math Scores')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.savefig('../../reports/figures/distribution_of_math_scores.png')
plt.show()

# 2. Boxplot of Writing Scores by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='gender', y='writing score')
plt.title('Writing Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Writing Score')
plt.savefig('../../reports/figures/writing_scores_by_gender.png')
plt.show()

# 3. Correlation Heatmap of Scores
plt.figure(figsize=(12, 8))
correlation_matrix = df[['math score', 'reading score', 'writing score']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Student Scores')
plt.savefig('../../reports/figures/correlation_heatmap.png')
plt.show()

# 4. Reading Score vs. Writing Score
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='reading score', y='writing score', hue='gender')
plt.title('Reading Score vs. Writing Score')
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.savefig('../../reports/figures/reading_vs_writing_score.png')
plt.show()

# 5. Math Score vs. Parental Level of Education
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='parental level of education', y='math score')
plt.title('Math Score by Parental Level of Education')
plt.xlabel('Parental Level of Education')
plt.ylabel('Math Score')
plt.xticks(rotation=45)
plt.savefig('../../reports/figures/math_score_by_parental_education.png')
plt.show()
