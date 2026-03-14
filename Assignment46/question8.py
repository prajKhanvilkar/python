import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def StudyHour():
    border = '-' * 40
    X = np.array( [1,2,3,4,5]).reshape((-1, 1))
    Y = np.array([50,55,60,65,70])
    print("Features",X.shape)
    print("Lables",Y.shape)
    print(border)
    print("Split the data in testing and training")
    X_train, X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
    print("Training dataset features", X_train.shape)
    print("Training dataset Lables", Y_train.shape)
    print("Testing dataset features", X_test.shape)
    print("Testing dataset lables", Y_test.shape)
    print(border)
    print("Train the model")
    model = LinearRegression()
    model.fit(X_train,Y_train)
    print("model trained Successfully")
    print(border)
    print(f"Intercept (b0): {model.intercept_}")
    print(f"Coefficient (b1): {model.coef_}")
    print(border)
    print("Test the model")
    Y_pred = model.predict(X_test)
    print("Predicted OutPut", Y_pred)
    print(border)
    new_experience = np.array([6]).reshape((-1, 1))
    predicted_salaries = model.predict(new_experience)
    print(f"Predicted salaries: {predicted_salaries}")
    print(border)


def main():
    StudyHour()

if __name__ == "__main__":
    main()