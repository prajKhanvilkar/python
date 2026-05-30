import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    #-------------------------------------------
    # step 1: Load Dataset
    #-------------------------------------------
    df = pd.read_csv("Mall_Customers.csv")
    print(df.head())
    print(df.shape)
    print(df.isnull().sum())
    #-------------------------------------------
    # step 2: Select Features
    #-------------------------------------------  
    print("Step 2: Select Features")      
    X = df[["AnnualIncome", "SpendingScore"]]
    print("Selected features")
    print(X.head())
    print("Shape of Selected features")
    print(X.shape)
if __name__ == "__main__":
    main()