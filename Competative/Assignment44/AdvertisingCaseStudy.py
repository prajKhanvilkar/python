import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def marvelousPredicter(DataPath):
    border = '-' *40
    print("Advertising Case Study")
    print(border)
    df = pd.read_csv(DataPath)
   
    print("First few records are")
    print(df.head())
    print(border)
    print("Data set before column removal")
    print(df.shape)
    print("Remove unnamed column")
    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0'], inplace=True)
    print("Data set after column removal")
    print(df.shape)
    print(border)
    print("Remove any missing value")
    print(df.isnull().sum())
    print(border)
    print("split the data set into features and lables")
    X = df[["TV","radio","newspaper"]]
    Y = df['sales']
    print("Features are:",X.shape)
    print('Label is', Y.shape)
    print(border)
    print("split data into testdata and train data")
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("X_train",X_train)
    print("Y_train",Y_train)
    print("X_test",X_test)
    print("Y_test",Y_test)
    print(border)
    print("train the model")
    model = LinearRegression()
    model.fit(X_train,Y_train)
    print("Model trained Successfully")
    print(border)
    print("Test the model")
    Y_pred = model.predict(X_test)
    
    print("Predicted value is :\n", Y_pred)
    print("Actual value is :\n",Y_test )
    print(border)


def main():
    marvelousPredicter("Advertising.csv")

if __name__ == "__main__":
    main()