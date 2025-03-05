import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    print("Dataset Loaded Successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display basic dataset info
print("\nFirst 5 rows of dataset:")
print(df.head())

# Basic Statistics
print("\nBasic Statistics:")
print(df.describe())

# Grouping Data
print("\nAverage Sepal Length per Species:")
grouped_data = df.groupby('species').mean()
print(grouped_data[['sepal length (cm)']])

# Data Visualization
sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))

# Line Chart
plt.subplot(2, 2, 1)
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.title("Line Chart - Sepal & Petal Length")
plt.legend()

# Bar Chart
plt.subplot(2, 2, 2)
sns.barplot(x='species', y='sepal length (cm)', data=df)
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.title("Bar Chart - Avg Sepal Length per Species")

# Histogram
plt.subplot(2, 2, 3)
plt.hist(df['petal length (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram - Petal Length Distribution")

# Scatter Plot
plt.subplot(2, 2, 4)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Scatter Plot - Sepal vs. Petal Length")

plt.tight_layout()
plt.show()

# Observations
print("\nObservations:")
print("1. Virginica species tend to have the largest sepal and petal length.")
print("2. Setosa species have the smallest petal length, making them easily distinguishable.")
print("3. The histogram shows a skewed distribution for petal length, indicating variations in species.")
print("4. The scatter plot indicates a correlation between sepal length and petal length, especially for Versicolor and Virginica species.")
