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
    




def main():
    marvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()