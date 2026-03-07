import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def marvellousPredictor():
    X = np.array( [1,2,3,4,5]).reshape((-1, 1))
    y = np.array([20000,25000,30000,35000,40000])

    model = LinearRegression().fit(X,y)

    print(f"Intercept (b0): {model.intercept_}")
    print(f"Coefficient (b1): {model.coef_}")

    new_experience = np.array([6]).reshape((-1, 1))
    predicted_salaries = model.predict(new_experience)

    print(f"Predicted salaries: {predicted_salaries}")

    plt.scatter(new_experience, predicted_salaries, color='red', label='Actual Data')
    plt.plot(X, y, color='blue', linewidth=2, label='Regression Line') 
    plt.title('Salary vs Experience (Linear Regression)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()

    

def main():
    marvellousPredictor()

if __name__ == "__main__":
    main()