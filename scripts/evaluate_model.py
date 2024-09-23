import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load the test data and model
X_test = pd.read_csv('data/X_test.csv')
y_test = pd.read_csv('data/y_test.csv')
model = joblib.load('models/popularity_model.pkl')

# Predict and evaluate
y_pred = model.predict(X_test)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Engagement Rate")
plt.ylabel("Predicted Engagement Rate")
plt.title("Model Evaluation")
plt.show()
