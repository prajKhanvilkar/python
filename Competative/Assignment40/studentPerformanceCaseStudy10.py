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
DataSet = "student_performance_ml3.csv"
df = pd.read_csv(DataSet)
feature_cols = ['StudyHours','PerformanceIndex' ,'Attendance', 'PreviousScore', 'AssignmentsCompleted','SleepHours']
 
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
                max_depth=None,
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

train_accuracy = accuracy_score(Y_train, model.predict(X_train))
print("Accuracy of the model on training data:", train_accuracy*100)

test_accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of the model on testing data:", test_accuracy*100)

print(border)
print("Its because we have changed the tuining parameter max_depth to None, which allows the decision tree to grow until all leaves are pure or until all leaves contain less than the minimum number of samples required to split. This can lead to overfitting, where the model performs well on the training data but poorly on unseen data. In this case, the model may have memorized the training data, resulting in a high training accuracy but a lower testing accuracy.")
