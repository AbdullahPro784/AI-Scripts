import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

print("Generating dataset...\n")

# 1. Create a mock dataset
np.random.seed(42)
n_students = 100

data = {
    'Student ID': range(1, n_students + 1),
    'Daily Social Media Hours': np.random.uniform(0.5, 6.0, n_students).round(1),
    'Study Hours': np.random.uniform(1.0, 6.0, n_students).round(1),
    'Sleep Hours': np.random.uniform(5.0, 9.0, n_students).round(1),
}

#create gpa score
gpa_base = 3.2
gpa = (gpa_base
       - 0.15 * data['Daily Social Media Hours']
       + 0.15 * data['Study Hours']
       + 0.10 * (data['Sleep Hours'] - 7))

# Ensure GPA stay within realistic 1.0 to 4.0 range
data['GPA'] = np.clip(gpa, 1.0, 4.0).round(2)

# Create the DataFrame i.e df
df = pd.DataFrame(data)

# 2. Inspect Dataset
print("--- Initial Data Inspection ---")
print(df.head())
print("\nDataset Info:")
print(df.info())

# 3. Data Cleaning (Check missing/duplicates)
print("\n--- Data Cleaning ---")
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)
print(f"Number of duplicate rows: {df.duplicated().sum()}")
df = df.dropna().drop_duplicates()

# 4. Descriptive Statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

avg_social_media = df['Daily Social Media Hours'].mean()
avg_gpa = df['GPA'].mean()
print(f"\nAverage Daily Social Media Hours: {avg_social_media:.2f}")
print(f"Average GPA: {avg_gpa:.2f}")

# 5. Highest and Lowest GPA Students
highest_gpa_student = df.loc[df['GPA'].idxmax()]
lowest_gpa_student = df.loc[df['GPA'].idxmin()]

print("\n--- Student Extremes ---")
print("Student with the Highest GPA:")
print(highest_gpa_student[['Student ID', 'GPA', 'Daily Social Media Hours']])
print("\nStudent with the Lowest GPA:")
print(lowest_gpa_student[['Student ID', 'GPA', 'Daily Social Media Hours']])

# 6. Group Comparison (< 3 hours vs >= 3 hours)
low_social_users = df[df['Daily Social Media Hours'] < 3]
high_social_users = df[df['Daily Social Media Hours'] >= 3]

print("\n--- GPA Comparison by Social Media Usage ---")
print(f"Average GPA (Less than 3 hours/day): {low_social_users['GPA'].mean():.2f}")
print(f"Average GPA (3 or more hours/day): {high_social_users['GPA'].mean():.2f}")

# 7. Correlation Analysis
print("\n--- Correlation with GPA ---")
analysis_cols = ['Daily Social Media Hours', 'Study Hours', 'Sleep Hours', 'GPA']
correlation_matrix = df[analysis_cols].corr()

gpa_correlations = correlation_matrix['GPA'].drop('GPA')
print(gpa_correlations)

strongest_var = gpa_correlations.abs().idxmax()
strongest_val = gpa_correlations[strongest_var]
print(f"\nThe variable with the strongest relationship to GPA is '{strongest_var}' (Correlation: {strongest_val:.3f})")

# 8. Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='Daily Social Media Hours',
    y='GPA',
    alpha=0.7,
    color='royalblue',
    edgecolor='w',
    s=70
)

# Add Scikit-learn trendline
X = df[['Daily Social Media Hours']]
y = df['GPA']
reg = LinearRegression().fit(X, y)
trendline = reg.predict(X)
plt.plot(df['Daily Social Media Hours'], trendline, color='red', linewidth=2, label='Trendline (Linear Regression)')

plt.title('Does Social Media Usage Affect Academic Performance?', fontsize=14, pad=15)
plt.xlabel('Daily Social Media Hours', fontsize=12)
plt.ylabel('GPA', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 9. Interpretation of Results
print("\n--- Interpretation of Results ---")

social_gpa_corr = gpa_correlations['Daily Social Media Hours']

print(f"Social Media Hours vs GPA correlation: {social_gpa_corr:.3f}")

if social_gpa_corr < 0:
    print("Interpretation: There is a negative relationship between social media usage "
          "and GPA. In this dataset, students who spend more time on social media "
          "tend to have lower GPAs.")
elif social_gpa_corr > 0:
    print("Interpretation: There is a positive relationship between social media usage "
          "and GPA. In this dataset, students who spend more time on social media "
          "tend to have higher GPAs.")
else:
    print("Interpretation: There is little to no linear relationship between social "
          "media usage and GPA.")

low_avg = low_social_users['GPA'].mean()
high_avg = high_social_users['GPA'].mean()

print(f"\nStudents using social media less than 3 hours/day have an average GPA of {low_avg:.2f}.")
print(f"Students using social media 3 or more hours/day have an average GPA of {high_avg:.2f}.")

if low_avg > high_avg:
    print("The less-than-3-hours group has the higher average GPA.")
elif high_avg > low_avg:
    print("The 3-or-more-hours group has the higher average GPA.")
else:
    print("Both groups have the same average GPA.")

print(f"\nThe strongest correlation with GPA is {strongest_var}, "
      f"with a correlation of {strongest_val:.3f}.")

print("\nOverall conclusion:")
print("The analysis shows an association between social media usage and academic "
      "performance in this simulated dataset. However, correlation does not prove "
      "that social media usage directly causes changes in GPA.")
