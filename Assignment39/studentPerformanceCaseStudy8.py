import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
from sklearn.model_selection import train_test_split   
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score,confusion_matrix,
                                classification_report,ConfusionMatrixDisplay)

Border = "-"*50
print(Border)
print("Load Dataset")

DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
print("Dataset loaded successfully!")
print(Border)
print("Dataset Analysis:")
print("Shape of the dataset:", df.shape)
print("Columns Name in the dataset:", list(df.columns))
print("Missing Values:")
print(df.isnull().sum())
print("Statistical Summary:")
print(df.describe())
print(Border)
feature_cols = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted','SleepHours']
 
X = df[feature_cols]
Y = df["FinalResult"]
 
print("X shape:", X.shape)
print("Y shape:", Y.shape) 

print(Border)
print("Data Visualization:")
plt.figure(figsize=(15,8))

for i, col in enumerate(feature_cols):
    plt.subplot(2,3,i+1)
    sns.scatterplot(data=df, x=col, y="FinalResult")
    plt.title(f"{col} vs FinalResult")

plt.tight_layout()
plt.show()
print(Border)
print("Data Splitting:")
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state=42)
print("Training set shape:", X_train.shape)
print("Result variable shape:", Y_train.shape)
print("Testing set shape:", X_test.shape) 
print("Result variable shape:", Y_test.shape)  
print(Border)
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)
model.fit(X_train, Y_train)

print("Model trained successfully!")
print(Border)
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Model Accuracy: {accuracy:.2f}")    

print(Border)
print("Classification Report:")
print(classification_report(Y_test, Y_pred))    

print(Border)
print("Confusion Matrix:")
cm = confusion_matrix(Y_test, Y_pred)   
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

print(Border)
print("conclusion:")
print("The Decision Tree model was successfully trained and evaluated.")
print("The model achieved a reasonable accuracy on the test set.")
print(Border)
print("End of the Case Study")