import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def StudyHour():
    border = '-' * 40
    X = np.array([[1,7],[2,6],[3,7],[4,6],[5,8]])
    Y = np.array([50,55,60,65,70])
    print("Features",X.shape)
    print("Lables",Y.shape)
    print(border)
    print("Train the model")
    model = LinearRegression()
    model.fit(X,Y)
    print("model trained Successfully")
    print(border)
    print(f"Intercept (b0): {model.intercept_}")
    print(f"Coefficient (b1): {model.coef_}")
    print(border)


def main():
    StudyHour()

if __name__ == "__main__":
    main()