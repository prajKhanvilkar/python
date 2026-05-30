import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def MarvellousPredictor():
    # Load the dataset
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independt variables X:",X)
    print("Values of Dependt variables y:",Y)
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    print("Mean of X:",mean_X)  #3.0
    print("Mean of Y:",mean_Y)  #3.6

    n = len(X) #5
    # y = m*x + c
    # m = (n*sum(x*y) - sum(x)*sum(y)) / (n*sum(x^2) - (sum(x))^2)
    # or
    # m = (sum(X-X_bar)* (Y-Y_bar)) / (sum(X-X_bar)**2)
    # c = (sum(y) - m*sum(x)) / n   

    # m = (n*sum(np.multiply(X,Y)) - sum(X)*sum(Y)) / (n*sum(np.multiply(X,X)) - (sum(X))**2)
    # c = (sum(Y) - m*sum(X)) / n

    numerator = 0
    denominator = 0
    for i in range(n):
        numerator = numerator + ((X[i] - mean_X) * (Y[i] - mean_Y))
        denominator = denominator + ((X[i] - mean_X) ** 2)

    m = numerator / denominator
    c = mean_Y - (m * mean_X)

    print("Slope of line(m):",m)
    print("Intercept (c):",c)
    

def main():
    MarvellousPredictor()
if __name__ == "__main__":
    main()