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

    numerator = 0
    denominator = 0
    for i in range(n):
        numerator = numerator + ((X[i] - mean_X) * (Y[i] - mean_Y))
        denominator = denominator + ((X[i] - mean_X) ** 2)

    m = numerator / denominator
    C = mean_Y - (m * mean_X)

    print("Slope of line(m):",m)
    print("Intercept (c):",C)

    x = np.linspace(1,6,n)
    print("x:",x)
    y = C+ m*x

    plt.plot(x,y,color='g',label='Regression Line')
    plt.scatter(X,Y,color='r',label='Scatter Plot')
    plt.xlabel('X: Independent variables')
    plt.ylabel('Y: Dependent variables')
    plt.legend()
    plt.show()

    # calculate yp and r squared
def main():
    MarvellousPredictor()
if __name__ == "__main__":
    main()