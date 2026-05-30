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
plt.title("Iris: petal length vr petal width")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.legend()
plt.grid(True)
plt.show()

####################################################################
#step5: Split Data Set for training and testing
########################################################################
print(Border)
print("Step 5: Split Data Set for training and testing")
print(Border)

#Test size = 20%
#train size = 80%

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

####################################################################
#step6: Build the model
########################################################################
print(Border)
print("Step 6: Build the model")
print(Border)

print("We are going to use Decission Tree Classifier")

model = DecisionTreeClassifier(
                criterion="gini",
                max_depth=4,
                random_state=42
)

print("Model created successfully!", model)

####################################################################
#step7: Train the model
########################################################################
print(Border)
print("Step 7: Train the model")
print(Border)

model.fit(X_train, Y_train)
print("Model trained Completed!")

####################################################################
#step8: Evaluate the model
########################################################################
print(Border)
print("Step 8: Evaluate the model")
print(Border)
Y_pred = model.predict(X_test)

print("Model Evaluation(testing) complete")

# print("Expected output:")
# print(Y_test.shape)
# print(Y_test)
print("Predicted output:")
print(Y_pred.shape)
print(Y_pred)

####################################################################
#step9: Evaluate the model performance
########################################################################
print(Border)
print("Step 9: Evaluate the model performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of the model:", accuracy*100)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix:")
print(cm)


print("Classification Report:")
print(classification_report(Y_test, Y_pred))    

####################################################################
#step10:Plot Confusion Matrix
########################################################################
print(Border)
print("Step 10: Plot Confusion Matrix")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
data.plot()
plt.title("Confusion Matrix of Iris Data Set")
plt.show()