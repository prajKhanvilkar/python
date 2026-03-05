import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score, mean_squared_error


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

    X= np.linspace(1,6,n)
    print("x:",X)
    Y = c + m*X
    plt.plot(X,Y,color='g',label = "Regression Line")
    plt.scatter(x,y,color='r', label = "Scatter Plot")
    plt.xlabel('X: Independent Variables')
    plt.ylabel('Y: Dependent Variables')
    plt.legend()
    plt.show()
    yPredicted = list()
    print("All Y values are")
    for i in range(len(x)):
        Y = c+m*x[i]
        yPredicted.append(Y)
    print("Predicted value of Y:", Y)
    meanSquared = mean_squared_error(y,yPredicted)
    print("Mean squared Error value", meanSquared)
    rSquare = r2_score(y,yPredicted)
    print("R squared value", rSquare)

def main():
    marvellousPredictor()

if __name__ == "__main__":
    main()