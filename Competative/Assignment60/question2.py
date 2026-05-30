# ---------------------------------------------------------
# Program : Program to create a single neuron and perform 
# forward pass with different activation functions and plot them
# Author  : Prajakta Khanvilkar
# ---------------------------------------------------------
import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return 1/(1+math.exp(-z))

def relu(z):
    return max(0,z)

def tanh(z):
    return (math.exp(z) - math.exp(-z)) / (math.exp(z) + math.exp(-z))

def Neuroun_forward (inputs, weights, bias, activationFunction):
    z = sum(w*x for w, x in zip(weights, inputs)) + bias
    print("weighted Sum ",z)
    y = activationFunction(z)
    print("Output after activation ",y)

def plot_activation_functions():

    z_values = np.linspace(-10, 10, 200)

    # Vectorized versions
    sigmoid_values = 1 / (1 + np.exp(-z_values))
    relu_values = np.maximum(0, z_values)
    tanh_values = np.tanh(z_values)
    plt.figure(figsize=(8, 5))

    # Plot both functions
    plt.plot(z_values, sigmoid_values, label="Sigmoid", linewidth=2)
    plt.plot(z_values, relu_values, label="ReLU", linewidth=2)
    plt.plot(z_values, tanh_values, label="Tanh", linewidth=2)

    # Reference lines
    plt.axhline(y=0, linewidth=0.5)
    plt.axhline(y=1, linewidth=0.5)
    plt.axvline(x=0, linestyle="--")

    # Labels
    plt.title("Sigmoid vs ReLU  vs Tanh Activation Functions", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()

def main():
    inputs = [-10,-5,-2,0,2, 3]
    weights = [0.2,0.3,0.1,0.4, 0.6]
    bias = 0.5
    print("=== Sigmoid Neuron ===")
    Neuroun_forward(inputs, weights, bias, sigmoid)

    # ReLU neuron
    print("=== ReLU Neuron ===")
    Neuroun_forward(inputs, weights, bias, relu)

    # Tanh neuron
    print("=== Tanh Neuron ===")
    Neuroun_forward(inputs, weights, bias, tanh)

    plot_activation_functions()

    print("\n Sigmoid is used for binary classification as its output range is between 0 to 1")
    print("\n\nReLU is used in hidden layers of neural networks, its output is 0 for negative inputs and linear for positive inputs, which helps to mitigate the vanishing gradient problem")
    print("\n\nTanh is used in hidden layers of neural networks, its output range is between -1 to 1, which can help to center the data and improve convergence during training")

if __name__ == "__main__":
    main()
