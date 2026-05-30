import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    #-------------------------------------------
    # step 1: Load Dataset
    #-------------------------------------------
    print("Step 1: Load Data")      
    df = pd.read_csv("Mall_Customers.csv")
    print("Initial few records are")
    print(df.head())
    print("Shape of the data")
    print(df.shape)
    print("Missing column in dataset")
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

    #-------------------------------------------
    # step 3: Scale the data
    #------------------------------------------- 
    print("Step 3: Scale the data")      
    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("data after scalling: ")
    print(X_scaled[:5])


if __name__ == "__main__":
    main()