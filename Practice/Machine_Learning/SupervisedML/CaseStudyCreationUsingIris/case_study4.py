import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (accuracy_score,confusion_matrix,
                              classification_report,ConfusionMatrixDisplay)

Border = '-'*50
####################################################################
#step1: Load the dataset
########################################################################
print(Border)
print("Step 1: Load the dataset")
print(Border)
Datasetpath = 'iris.csv'
df = pd.read_csv(Datasetpath)
print("Dataset loaded successfully!")
print("Intial enteries from dataset:")
print(df.head())
####################################################################
#step2: Data Analysis (EDA)
########################################################################
print(Border)
print("Step 2: Data Analysis (EDA)")
print(Border)

print("shape of dataset:", df.shape)
print("column names:", list(df.columns))
print('missing values :')
print(df.isnull().sum())

print("Class distribution species count:")
print(df["species"].value_counts())

print("Statistical summary of dataset:")
print(df.describe())

####################################################################
#step3: Decide independent and dependent variables
########################################################################
print(Border)
print("Step 3: Decide independent and dependent variables")
print(Border)

#X:Independent variables or features
#Y:Dependent variables or labels
feature_cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

X = df[feature_cols]
Y = df["species"]

print("X shape:", X.shape)
print("Y shape:", Y.shape)  

####################################################################
#step4: Visualization of dataset
########################################################################
print(Border)
print("Step 4: Visualization of dataset")
print(Border)

#scatter Plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label=sp)
plt.title("Iris: petal length vr petal wid  th")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.legend()
plt.grid(True)
plt.show()

