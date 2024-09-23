import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the collected data
df = pd.read_csv('data/videos.csv')

# Feature engineering: create engagement rate feature
df['engagement_rate'] = (df['likes'] + df['comments'] + df['shares']) / df['views']

# Handle missing values, outliers, etc.
df = df.dropna()  # Example: drop rows with missing values

# Text preprocessing: Optional step
df['description_length'] = df['description'].apply(lambda x: len(str(x).split()))

# Create training and test datasets
features = ['description_length', 'views', 'followers']  # Add more features as needed
target = 'engagement_rate'
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save preprocessed data
X_train.to_csv('data/X_train.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
X_test.to_csv('data/X_test.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)

print("Data preprocessing complete.")
