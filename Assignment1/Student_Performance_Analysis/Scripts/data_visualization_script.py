import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the current script directory
visualizations_dir = os.path.join(base_dir, '../Visualizations')  # Path to the Visualizations folder

# Load the dataset
data = pd.read_csv('Data/StudentsPerformance.csv')

# Create a new column for average score
data['average_score'] = data[['math score', 'reading score', 'writing score']].mean(axis=1)

# 1. Distribution of Student Average Scores (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(data['average_score'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Student Average Scores')
plt.xlabel('Average Score')
plt.ylabel('Frequency')
plt.savefig(os.path.join(visualizations_dir, 'average_score_distribution_histogram.png'))
plt.close()

# 2. Comparison of Average Scores by Gender (Box Plot)
plt.figure(figsize=(10, 6))
data.boxplot(column='average_score', by='gender', grid=False)
plt.title('Comparison of Average Scores by Gender')
plt.suptitle('')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.savefig(os.path.join(visualizations_dir, 'average_scores_by_gender_boxplot.png'))
plt.close()

# 3. Average Scores by Parental Education Level (Bar Chart)
avg_scores = data.groupby('parental level of education')['average_score'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_scores.plot(kind='bar', color='lightgreen')
plt.title('Average Scores by Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.savefig(os.path.join(visualizations_dir, 'parental_education_average_scores_bar_chart.png'))
plt.close()

# 4. Heatmap of Average Scores Across Gender and Parental Education
heatmap_data = data.pivot_table(values='average_score', index='gender', columns='parental level of education')
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True)
plt.title('Heatmap of Average Scores Across Gender and Parental Education')
plt.savefig(os.path.join(visualizations_dir, 'average_scores_heatmap.png'))
plt.close()

# 5. Average Scores by Test Preparation Course (Bar Chart)
avg_scores_prep = data.groupby('test preparation course')['average_score'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_scores_prep.plot(kind='bar', color='lightcoral')
plt.title('Average Scores by Test Preparation Course')
plt.xlabel('Test Preparation Course')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.savefig(os.path.join(visualizations_dir, 'average_scores_by_test_preparation_course.png'))
plt.close()
