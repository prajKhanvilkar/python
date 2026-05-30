import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
def marvellousPredict(DataFile):
    border ="-"*40

    #----------------------------------------------------
    #step1: read Data from the csv file
    #----------------------------------------------------
    print(border)
    print("Step1: Read Data from the csv file")
    print(border)
    df = pd.read_csv(DataFile)
    print("first few records from dataset")
    print(df.head())
    print("Dataset shape:")
    print(df.shape)

    #----------------------------------------------------
    #step2: Remove unwanted colums
    #----------------------------------------------------
    print(border)
    print("Step2: Remove unwanted colums")
    print(border)

    print("shape of Dataset before removal",df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)
    print("shape of Dataset after removal",df.shape)
    
    print(border)
    print("Clean dataset is")
    print(border)

    print(df.head())

    #----------------------------------------------------
    #step3: Check for missing Values
    #----------------------------------------------------
    print(border)
    print("Step3: Check for missing Values")
    print(border)
    print("Missing values in dataset:")
    print(df.isnull().sum())

    #----------------------------------------------------
    #step4: Encode the Columns of Weather and Temperature
    #----------------------------------------------------
    print(border)
    print("Step4: Encode the Columns of Weather")
    print(border)
    
    le = LabelEncoder()

    df['Whether'] = le.fit_transform(df['Whether'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    

    #----------------------------------------------------
    #step5: Summary of dataset
    #----------------------------------------------------
    print(border)
    print("Step5: Summary of dataset")
    print(border)
    print("Summary of dataset:")
    print(df.describe())

    #----------------------------------------------------
    #step6: Split the data into features and target variable
    #----------------------------------------------------
    print(border)
    print("Step6 : Split the data into features and target variable")
    print(border)

    X = df[["Whether","Temperature"]]
    Y = df["Play"]

    print("Features:", X.shape)
    print("Labels:",Y.shape)
    #----------------------------------------------------
    #step6 : Split the data in train and test
    #----------------------------------------------------
    print(border)
    print("Step6 :  Split the data in train and test")
    print(border)
   
    X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X train:", X_train.shape)
    print("X test:", X_test.shape)
    print("Y train:", Y_train.shape)
    print("Y test:", Y_test.shape)
    
    #----------------------------------------------------
    #step7 : Train the model
    #----------------------------------------------------
    print(border)
    print("Step7 : Train the model")
    print(border)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)

    #----------------------------------------------------
    #step8 : Test the Model
    #----------------------------------------------------
    print(border)
    print("Step8 : Test the model")
    print(border)

    Y_pred = model.predict(X_test)
    print("Predicted output:")
    print(Y_pred.shape)
    print(Y_pred)

    #----------------------------------------------------
    #step9 : Calculate Accuracy
    #----------------------------------------------------
    print(border)
    print("Step9 : Calculate Accuracy")
    print(border)
    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of the model is :", accuracy % 100)
    


def main():
    marvellousPredict("PlayPredictor.csv")

if __name__ == "__main__":
    main()