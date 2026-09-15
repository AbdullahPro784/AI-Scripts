# 📊 Does Social Media Usage Affect Academic Performance?

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-Machine_Learning-F7931E)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blueviolet)

## 📝 Overview
This Python-based research project investigates the relationship between the amount of time students spend on social media and their overall academic performance (GPA). Using a synthetic dataset of 100 students, the project applies data manipulation, statistical analysis, and data visualization techniques to uncover trends and correlations among daily habits and academic success.

## ✨ Key Features
- **Data Generation & Cleaning:** Simulates a realistic dataset (Student ID, Social Media Hours, Study Hours, Sleep Hours, GPA) and ensures data integrity by checking for missing and duplicate values.
- **Exploratory Data Analysis (EDA):** Calculates descriptive statistics, averages, and identifies students with the highest and lowest GPAs.
- **Comparative Analysis:** Compares the average GPA of moderate social media users (< 3 hours/day) against heavy users (≥ 3 hours/day).
- **Correlation Matrix:** Computes Pearson correlation coefficients to determine which lifestyle factor has the strongest impact on GPA.
- **Data Visualization:** Generates a scatter plot with a Scikit-Learn linear regression trendline to visually represent the relationship between social media usage and grades.

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/social-media-gpa-analysis.git
   cd social-media-gpa-analysis
   ```

2. **Install the required dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

3. **Run the analysis script:**
   ```bash
   python script.py
   ```

## 📈 Results & Visualization

Here is the scatter plot demonstrating the relationship between daily social media hours and GPA:

> 🖼️ **Note:** Replace the image path below with the actual screenshot of your graph.

![Scatter Plot: Social Media Usage vs GPA](path/to/your/screenshot.png)

### 🧠 Interpretation of Findings
- **Negative Correlation:** There is a clear negative correlation between Daily Social Media Hours and GPA. The downward trend indicates that as time spent on social media increases, academic performance tends to decrease.
- **User Groups:** Students who spent less than 3 hours per day on social media demonstrated a noticeably higher average GPA compared to those who spent 3 or more hours.
- **Strongest Predictor:** When comparing all variables (Social Media, Study, and Sleep hours), Social Media Hours had the strongest overall relationship (a negative correlation) with a student's GPA, making it the most significant predictor of academic performance in this dataset.

## 🛠️ Technologies Used
* **Python:** Core programming language.
* **Pandas & NumPy:** Data creation, manipulation, and statistical calculations.
* **Matplotlib & Seaborn:** Data visualization and plot styling.
* **Scikit-learn:** Implementing linear regression for the trendline.

---
*Developed for an Academic Data Analysis Assignment.*
