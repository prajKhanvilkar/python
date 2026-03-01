import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score,confusion_matrix,
                              classification_report,ConfusionMatrixDisplay)

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
print(df.head())
feature_cols = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted','SleepHours']
 
X = df[feature_cols]
Y = df["FinalResult"]
 
print("X shape:", X.shape)
print("Y shape:", Y.shape)  
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)
 
print("Independent:",X.shape)
print("Dependent:",Y.shape)
print("Data Splitting Activity:")
print("X_train shape:", X_train.shape)
print("Y_train shape:", Y_train.shape)
print("X_test shape:", X_test.shape)
print("Y_test shape:", Y_test.shape)

print(border)
 
print("We are going to use Decission Tree Classifier")
 
model = DecisionTreeClassifier(
                criterion="gini",
                max_depth=4,
                random_state=42
)
 
print("Model created successfully!", model)

model.fit(X_train, Y_train)
print("Model trained Completed!")
sampleData = [
    {'StudyHours': 6, 'Attendance': 85, 'PreviousScore': 66, 'AssignmentsCompleted': 7, 'SleepHours': 7},
    {'StudyHours': 7, 'Attendance': 45, 'PreviousScore': 33, 'AssignmentsCompleted': 4, 'SleepHours': 6},
    {'StudyHours': 8, 'Attendance': 55, 'PreviousScore': 45, 'AssignmentsCompleted': 5, 'SleepHours': 2},
    {'StudyHours': 3, 'Attendance': 65, 'PreviousScore': 43, 'AssignmentsCompleted': 7, 'SleepHours': 5},
    {'StudyHours': 4, 'Attendance': 75, 'PreviousScore': 66, 'AssignmentsCompleted': 2, 'SleepHours': 3}
]

input_data = pd.DataFrame(sampleData)

# Ensure column order matches training data
input_data = input_data[feature_cols]

predictions = model.predict(input_data)

print("Predictions:", predictions)