# ---------------------------------------------------------
# Program : Program to create a single neuron and perform forward pass
# Author  : Prajakta Khanvilkar
# ---------------------------------------------------------
import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return 1/(1+math.exp(-z))

def Neuroun_forward (imputs, weights, bias):
    z = sum(w*x for w, x in zip(weights, imputs)) + bias
    print("weighted Sum ",z)
    y = sigmoid(z)
    return z,y

def main():
    imputs = [2, 3]
    weights = [ 0.4, 0.6]
    bias = 0.5
    z, y = Neuroun_forward(imputs, weights, bias)
    
    print("Final z     :", z)
    print("Final y_hat :", y)

if __name__ == "__main__":
    main()
