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
    print("Mean of X:",mean_X)
    print("Mean of Y:",mean_Y)

    

def main():
    MarvellousPredictor()
if __name__ == "__main__":
    main()