import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv("Advertising.csv")
    print(df.shape)
    if "Unnamed: 0" in df.columns:
        df.drop(columns= ["Unnamed: 0"], inplace=True)
    print(df.shape)

    #Split the data into X, Y
    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Independent variables:",X.shape)
    print("Dependent variable: ",Y.shape)

    #split the data for training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1, random_state=42)

    model = LinearRegression()
    model.fit(X_train,Y_train)
    print("Model trained successfully")

    y_pred = model.predict(X_test)

    print("Testing Data")
    print(X_test)
    print("Predicted values:")
    print(y_pred)
    print("Actual values:")
    print(Y_test)
    print("Coefficient: ", model.coef_)
    print("Intercept: ", model.intercept_)



if __name__ == "__main__":
    main()