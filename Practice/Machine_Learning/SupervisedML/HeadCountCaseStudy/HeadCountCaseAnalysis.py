import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousPredictor(DataFile):
    border = "-"*40
    #-------------------------------------------------------
    #Step1: Load dataset
    #-------------------------------------------------------
    print(border)
    print("Step1 : Load Dataset ")
    print(border)
    df = pd.read_csv(DataFile)
    print("Few records from dataset")
    print(df.head())
    print("Shape of dataset:",df.shape)

    #-------------------------------------------------------
    #Step2: Check Missing Values
    #-------------------------------------------------------
    print(border)
    print("Step2: Check Missing Values")
    print(border)
    print("Missing Values Count: \n",df.isnull().sum())

    #-------------------------------------------------------
    #Step3: Display Statistical Summary
    #-------------------------------------------------------
    print(border)
    print("Step3: Display Statistical Summary")
    print(border)
    print(df.describe())

    #-------------------------------------------------------
    #Step4: Correlation Between Columns
    #-------------------------------------------------------
    print(border)
    print("Step4: Correlation Between Columns")
    print(border)
    print("Correlation Matrix: \n",df.corr())

    #-------------------------------------------------------
    #Step5: Split dataset into features and target variable
    #-------------------------------------------------------
    print(border)
    print("Step5: Split dataset into features and target variable")
    print(border)

    X= df[['Age Range', 'Head Size(cm^3)', 'Brain Weight(grams)']]
    Y = df['Gender']
    
    print('Independent Variables (X):', X.shape)
    print('Dependent Variable (Y):', Y.shape)

    #-------------------------------------------------------
    #Step6: Split dataset into training and testing sets
    #-------------------------------------------------------
    print(border)
    print("Step6: Split dataset into training and testing sets")
    print(border)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
    
    print("Training set - Independent Variables (X_train):", X_train.shape)
    print("Testing set - Independent Variables (X_test):", X_test.shape)        
    print("Training set - Dependent Variable (Y_train):", Y_train.shape)
    print("Testing set - Dependent Variable (Y_test):", Y_test.shape)

    #-------------------------------------------------------
    #Step7: Create and Train Model
    #-------------------------------------------------------
    print(border)
    print("Step7: Create and Train Model")
    print(border)
    model = LinearRegression()
    model.fit(X_train, Y_train)
    
    #-------------------------------------------------------
    #Step8: Make Predictions
    #-------------------------------------------------------
    print(border)
    print("Step8: Make Predictions")
    print(border)
    y_pred = model.predict(X_test)
    print("Predicted Values: \n", y_pred)
    print("Actual Values: \n", Y_test.values)
    
    #-------------------------------------------------------
    #Step9: Evaluate Model
    #-------------------------------------------------------
    print(border)
    print("Step9: Evaluate Model")
    print(border)

    mse = mean_squared_error(Y_test, y_pred)
    r2 = r2_score(Y_test, y_pred)
    print("Mean Squared Error (MSE):", mse)
    print("R-squared (R2):", r2)
    print(border)

    #-------------------------------------------------------
    #Step10: Visualization
    #-------------------------------------------------------
    print(border)
    print("Step10: Visualization")
    print(border)
    plt.figure(figsize=(8,5))
    plt.scatter(Y_test, y_pred)
    plt.xlabel("Actual Gender")
    plt.ylabel("Predicted Gender")
    plt.title("Actual vs Predicted Gender")
    plt.grid(True)
    plt.show()
    

def main():
    MarvellousPredictor("MarvellousHeadBrain.csv")

if __name__ == "__main__":
    main()