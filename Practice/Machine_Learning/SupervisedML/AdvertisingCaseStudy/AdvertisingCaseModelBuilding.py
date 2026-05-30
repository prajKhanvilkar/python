import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def marvellousAdvertise(DataPath):
    border = "-"*40
    #-------------------------------------------------------
    #Step1: Load dataset
    #-------------------------------------------------------
    print(border)
    print("Step1 : Load Dataset ")
    print(border)
    df = pd.read_csv(DataPath)
    print("Few records from dataset")
    print(df.head())

    #-------------------------------------------------------
    #Step2: Remove Unwanted columns
    #-------------------------------------------------------
    print(border)
    print("Step2: Remove unwanted columns")
    print(border)
    print("shape of Dataset before removal",df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)
    print("shape of Dataset after removal",df.shape)
    
    print(border)
    print("Clean dataset is")
    print(border)

    print(df.head())

    #-------------------------------------------------------
    #Step3: Check Missing Values
    #-------------------------------------------------------
    print(border)
    print("Step3: Check Missing Values")
    print(border)
    print("Missing Values Count:\n",df.isnull().sum())

    #-------------------------------------------------------
    #Step4: Display Statistical Summary
    #-------------------------------------------------------
    print(border)
    print("Step4: Display Statistical Summary")
    print(border)
    print(df.describe())

    #-------------------------------------------------------
    #Step5: Corelation Between Columns
    #-------------------------------------------------------
    print(border)
    print("Step5: Corelation Between Columns")
    print(border)
    print("Correlation Matrix")
    print(df.corr())

    #-------------------------------------------------------
    #Step6: Split Data
    #-------------------------------------------------------
    print(border)
    print("Step6: Split Data")
    print(border)
    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Independent variables:",X.shape)
    print("Dependent variable: ",Y.shape)

    #-------------------------------------------------------
    #Step7: Split Data for train and test
    #-------------------------------------------------------
    print(border)
    print("Step7: Split Data for train and test")
    print(border)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1, random_state=42)

    print("Dependent variable: ",X_train)
    print("Dependent variable: ",X_test)
    print("Dependent variable: ",Y_train)
    print("Dependent variable: ",Y_test)

    #-------------------------------------------------------
    #Step8: Create and Train Model 
    #-------------------------------------------------------
    print(border)
    print("Step8: Create and Train Model")
    print(border)
    model = LinearRegression()
    model.fit(X_train,Y_train)
    print("Model trained successfully")

    #-------------------------------------------------------
    #Step9:Test Model
    #-------------------------------------------------------
    print(border)
    print("Step9: Test Model")
    print(border)

    y_pred = model.predict(X_test)

    #-------------------------------------------------------
    #Step10:Evaluate the Model
    #-------------------------------------------------------
    print(border)
    print("Step10: Evaluate the Model")
    print(border)

    MSE = mean_squared_error(Y_test,y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, y_pred)

    print("Mean Squared Error:", MSE)
    print("Root Mean Squares Value:", RMSE)
    print("R Square Value:", R2)

    #-------------------------------------------------------
    #Step11:Calculate Model Coefficient
    #-------------------------------------------------------
    print(border)
    print("Step11:Calculate Model Coefficient")
    print(border)

    for column, value in zip(X.columns, model.coef_):
        print(f"{column} : {value}")
    
    print("intercept:", model.intercept_)


    #-------------------------------------------------------
    #Step12:Compare the actual and predicted values
    #-------------------------------------------------------
    print(border)
    print("Step12:Compare the actual and predicted values")
    print(border)
    Result = pd.DataFrame({
        'Actual Sale': Y_test.values,
        'Predicted Sale':y_pred})
    print(Result.head(10))

    #-------------------------------------------------------
    #Step13:Visualization
    #-------------------------------------------------------
    print(border)
    print("SStep13:Visualization")
    print(border)   
    
def main():
    marvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()