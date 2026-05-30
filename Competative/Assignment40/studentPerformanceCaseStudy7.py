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
 
print("We are going to use Decission Tree Classifier with random state 42")
 
model = DecisionTreeClassifier(
                criterion="gini",
                max_depth=4,
                random_state=42
)
 
print("Model created successfully!", model)

model.fit(X_train, Y_train)
print("Model trained Completed!")

Y_pred = model.predict(X_test)
 
print("Model Evaluation(testing) complete")

print("Predicted output:")
print(Y_pred.shape)
print(Y_pred)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of the model:", accuracy*100)

print("Classification Report:")
print(classification_report(Y_test, Y_pred))    

print(border)
 
print("We are going to use Decission Tree Classifier with random state 0")
 
model = DecisionTreeClassifier(
                criterion="gini",
                max_depth=4,
                random_state=0
)
 
print("Model created successfully!", model)

model.fit(X_train, Y_train)
print("Model trained Completed!")

Y_pred = model.predict(X_test)
 
print("Model Evaluation(testing) complete")

print("Predicted output:")
print(Y_pred.shape)
print(Y_pred)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of the model:", accuracy*100)

print("Classification Report:")
print(classification_report(Y_test, Y_pred))    

print(border)
 
print("We are going to use Decission Tree Classifier with random state 10")
 
model = DecisionTreeClassifier(
                criterion="gini",
                max_depth=4,
                random_state=10
)
 
print("Model created successfully!", model)

model.fit(X_train, Y_train)
print("Model trained Completed!")

Y_pred = model.predict(X_test)
 
print("Model Evaluation(testing) complete")

print("Predicted output:")
print(Y_pred.shape)
print(Y_pred)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of the model:", accuracy*100)

print("Classification Report:")
print(classification_report(Y_test, Y_pred))    

print(border)
print("The model with all max depth has the Same accuracy of 93.33% , as the dataset is small and simple")