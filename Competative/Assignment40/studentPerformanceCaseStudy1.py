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

model_feature = model.feature_importances_
print("Feature importance:", model_feature)
feature_importance_series = pd.Series(model_feature, index=X.columns)
feature_importance_series = feature_importance_series.sort_values(ascending=False)
print("Feature importance series:\n", feature_importance_series)
print(border)
print("Attendance contributes the most to predicting the final result of the student.")
print("StudyHours and PreviousScore also have significant contributions, while SleepHours has the least contribution among the features.")
print(border)


