# ---------------------------------------------------------
# Program : Program to show flattening
# Author  : Prajakta Khanvilkar
# ---------------------------------------------------------

# ------------------------------------------------------------
# Step 1: Input 2D Matrix
# ------------------------------------------------------------
matrix = [
    [6, 4],
    [8, 6]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# ------------------------------------------------------------
# Step 2: Flatten (2D → 1D)
# ------------------------------------------------------------
flatten_output = []

for row in matrix:
    for val in row:
        flatten_output.append(val)

print("\nFlatten Output:")
print(flatten_output)

# ------------------------------------------------------------
# Step 3: Fully Connected Layer (Manual)
# ------------------------------------------------------------
# Assume weights and bias
weights = [0.5, -0.2, 0.3, 0.1]
bias = 1

print("\nWeights:", weights)
print("Bias:", bias)

# ------------------------------------------------------------
# Step 4: Output Calculation
# y = w1*x1 + w2*x2 + ... + bias
# ------------------------------------------------------------
output = 0

print("\n--- Calculation ---")

for i in range(len(flatten_output)):
    mul = flatten_output[i] * weights[i]
    print(f"{flatten_output[i]} * {weights[i]} = {mul}")
    output += mul

output += bias

print("\nFinal Output:", output)

# ------------------------------------------------------------
# Step 5: Explain the role of flatten layer in CNN
# ------------------------------------------------------------
# Flatten layer converts matrix into a vector so that it will be the input for the fully connected layer
# It just reshape the data without changing its values (without performing any operation)