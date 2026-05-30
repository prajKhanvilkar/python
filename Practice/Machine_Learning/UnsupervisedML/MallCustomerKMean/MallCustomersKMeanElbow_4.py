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

    #-------------------------------------------
    # step 4: Use Elbow method
    #------------------------------------------- 
    print("Step 4: Use Elbow method")      
    WCSS = []

    for i in range(1,11):
        model = KMeans(n_clusters=i,random_state=42, n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_) #WCSS =  within cluster sum of square

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11),WCSS,marker = 'o')
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    # plt.show()

    #-------------------------------------------
    # step 5: Train and test the model
    #------------------------------------------- 
    print("Step 5: Train and test the model")    

    model = KMeans(n_clusters=4,random_state=42,n_init=10)  
    clusters = model.fit_predict(X_scaled)

    df['clusters'] = clusters

    print("Data set with cluster")
    print(df.head())




if __name__ == "__main__":
    main()