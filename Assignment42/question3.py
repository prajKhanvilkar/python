import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def marvellousPredictor():
    # Sample data: Years of Experience (X) and Salary (Y)
    X = np.array( [1,2,3,4,5]).reshape((-1, 1))
    y = np.array([20000,25000,30000,35000,40000])

    model = LinearRegression().fit(X,y)
    # Print the intercept and slope
    print(f"Intercept (b0): {model.intercept_}")
    print(f"Coefficient (b1): {model.coef_}")

    # Predict the salary for someone with 7 and 8 years of experience
    new_experience = np.array([6]).reshape((-1, 1))
    predicted_salaries = model.predict(new_experience)

    print(f"Predicted salaries: {predicted_salaries}")


    plt.plot(X,y,color='g',label = "Regression Line")
    plt.scatter(new_experience,predicted_salaries,color='r', label = "Scatter Plot")
    plt.xlabel('X: Independent Variables')
    plt.ylabel('Y: Dependent Variables')
    plt.legend()
    plt.show()
    

def main():
    marvellousPredictor()

if __name__ == "__main__":
    main()