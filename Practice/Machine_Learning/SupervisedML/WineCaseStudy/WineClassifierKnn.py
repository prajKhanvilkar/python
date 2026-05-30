import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "-" * 40
    print(border)
    #Step 1: Load Dataset from CSV file
    print("Step 1: Load Dataset from CSV file")
    print(border)
    df = pd.read_csv(DataPath)
    print(df.shape)
    print("First few records in dataSet")
    print(df.head())
    print(border)
    #Step 2: Clean the Dataset by removing missing data
    print("Step 2: Clean the Dataset by removing missing data")
    print(border)
    print("Missing data")
    df.dropna(inplace=True)
    print("Total Records",df.shape[0])
    print("Total Column",df.shape[1])
    # print(df.isnull().sum())
    print(border)
    #Step 3: Split the data into Independent and Dependent
    print("Step 3: Split data into Independent and Dependent")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X",X.shape)
    print("Shape of Y",Y.shape)
    print(border)
    print("Input Columns:", X.columns.to_list())
    print("Output Column: Class")
    print(border)
    #Step 4: Split the data into Test and Train dataset
    print("Step 4: Split the data into Test and Train dataset")
    print(border)
    
    X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=42, stratify=Y)
    print(border)
    print("Information of training and testing data")
    print("shape of X_train",X_train.shape)
    print("Shape of X_test",X_test.shape)
    print("Shape of Y_train",Y_train.shape)
    print("Shape of Y_test",Y_test.shape)

    print(border)
    #Step 5: Feature Scalling
    print("Step 5: Feature Scalling")
    print(border)

    scaller = StandardScaler()
    X_train_scaled = scaller.fit_transform(X_train)
    X_test_scaled = scaller.fit_transform(X_test)

    print("Feature Scalling is Done")
    print(border)
    #Step6 : Explore Multiple values of K
    #Hyperparameter Tuning(K)
    print("Step6 :  Explore Multiple values of K")
    print(border)

    accuracy_scores = []
    k_values = range(1,21)

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy =  accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy Report of All K values from 1 to 20 ")
    for value in accuracy_scores:
        print(value)
    print(border)
    
    print(border)
    print("Step 7 : Plot graph of K vs Accuracy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(k_values, accuracy_scores, marker = 'o')
    plt.title("K vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(k_values))
    plt.show()

    #step 8: Find Best value of K
    print(border)
    print("Step 8: Find Best value of K ")
    print(border)

    best_k = list(k_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best Value of K is :", best_k)

    #Step 9 : Build Final model using best value of k
    print(border)
    print("#Step 9 : Build Final model using best value of k")
    print(border)
    finalmodel = KNeighborsClassifier(n_neighbors=best_k)
    finalmodel.fit(X_train_scaled,Y_train)
    Y_pred = finalmodel.predict(X_test_scaled)

    #Step 10 : Calculate Final Accuracy
    print(border)
    print("#Step 10 : Calculate Final Accuracy")
    print(border)
    accuracy =  accuracy_score(Y_test,Y_pred)
    print("Accuracy of final model is", accuracy %100)

    #step11 : Display Confusion Matrix
    print(border)
    print("#Step 11 : Display Confusion Matrix")
    print(border)

    cf = confusion_matrix(Y_test,Y_pred)
    print(cf)

    #step11 : Display Classification Report
    print(border)
    print("#Step 11 : Display Classification Report")
    print(border)

    print(classification_report(Y_test,Y_pred))

def main():
    border = "-" * 40
    print(border)
    print("Wine Classifier Using KNN")
    print(border)
    MarvellousClassifier('WinePredictor.csv')
    
if __name__ == "__main__":
    main()