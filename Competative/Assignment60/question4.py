# ---------------------------------------------------------
# Program : Program to create a single neuron and perform forward pass and backpropagation
# Author  : Prajakta Khanvilkar
# ---------------------------------------------------------
import math

def Sigmoid(value):
    return 1 / (1 + math.exp(-value))

def Sigmoid_Derivative(output):
    return output * (1 - output)

x1 = 1.0
x2 = 2.0
target = 1.0
w1 = 0.5
w2 = -0.3
b = 0.1
learning_rate = 0.1
epochs = 10

print("Initial Values")
print("w1 =", w1)
print("w2 =", w2)
print("b  =", b)
print("-" * 50)

for epoch in range(1, epochs + 1):
    z = (x1 * w1) + (x2 * w2) + b

    output = Sigmoid(z)
    loss = 0.5 * (target - output) ** 2

    dL_doutput = output - target

    doutput_dz = Sigmoid_Derivative(output)

    dL_dz = dL_doutput * doutput_dz

    dL_dw1 = dL_dz * x1
    dL_dw2 = dL_dz * x2
    dL_db = dL_dz

    w1 = w1 - (learning_rate * dL_dw1)
    w2 = w2 - (learning_rate * dL_dw2)
    b = b - (learning_rate * dL_db)

    print("Epoch:", epoch)
    print("Weighted Sum (z):", round(z, 4))
    print("Predicted Output :", round(output, 4))
    print("Target Output    :", target)
    print("Loss             :", round(loss, 6))
    print("Gradient dL/dw1  :", round(dL_dw1, 6))
    print("Gradient dL/dw2  :", round(dL_dw2, 6))
    print("Gradient dL/db   :", round(dL_db, 6))
    print("Updated w1       :", round(w1, 6))
    print("Updated w2       :", round(w2, 6))
    print("Updated b        :", round(b, 6))
    print("-" * 50)

print("Final Trained Values")
print("w1 =", round(w1, 6))
print("w2 =", round(w2, 6))
print("b  =", round(b, 6))