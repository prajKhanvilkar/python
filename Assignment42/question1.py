import numpy as np
import pandas as pd

def marvellousPredictor():
    x = [1,2,3,4,5]
    y = [3,4,2,4,5]
  
    meanX = np.mean(x)
    meanY = np.mean(y)
    print("Mean of X is:",meanX)
    print("Mean of Y:",meanY)

    n = len(x)
    numerator = 0
    denominator =0 
   
    for i in range(n):
        numerator = numerator + ((x[i] - meanX) * (y[i] - meanY))
        denominator = denominator + ((x[i] - meanX) ** 2)
 
    m = numerator/denominator
    c = meanY - (m * meanX)
    print("Slope of line (m) is :",m)
    print("Intercept (c)is; ",c)

def main():
    marvellousPredictor()

if __name__ == "__main__":
    main()