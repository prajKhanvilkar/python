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
    
if __name__ == "__main__":
    main()