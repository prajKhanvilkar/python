import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def WinePredictor(DataPath):
    border = '-' * 40
    df = pd.read_csv(DataPath)
    print("Wine Classsifier")
    print(border)
    print("Few Records from dataset")
    print(df.head())
    print(border)
    print("Check for the data having missing values")
    df.dropna(inplace=True)
    print("Dataset after removal")
    print(df.shape)
    print(border)
    print("Split Dataset ito features and Lables")
    X = df.drop(columns=['Class'])
    Y = df['Class']
    print("Features",X.shape)
    print("Lables",Y.shape)
    print(border)
    print("Split the data in testing and training")
    X_train, X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
    print("Training dataset features", X_train.shape)
    print("Training dataset Lables", Y_train.shape)
    print("Testing dataset features", X_test.shape)
    print("Testing dataset lables", Y_test.shape)
    print(border)
    print("Train the model")
    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)
    print("model trained Successfully")
    print(border)
    print("Test the model")
    Y_pred = model.predict(X_test)
    
    print("Predicted OutPut", Y_pred)
    print(border)
    print("Calculate Accurracy")
    Accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy is :",Accuracy% 100)
    print(border)




def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()