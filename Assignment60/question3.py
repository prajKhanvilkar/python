# ---------------------------------------------------------
# Program : Program to create a single neuron and calculate MSE and BCE loss functions
# Author  : Prajakta Khanvilkar
# ---------------------------------------------------------
import math

def calculate_mse(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    
    n = len(y_true)
    sum_squared_error = 0
    
    for i in range(n):
        error = y_true[i] - y_pred[i]
        sum_squared_error += error ** 2
    
    mse = sum_squared_error / n
    return mse


def calculate_binary_cross_entropy(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    
    n = len(y_true)
    sum_entropy = 0
    epsilon = 1e-15  # Small value to avoid log(0)
    
    for i in range(n):
        y_pred_clipped = max(epsilon, min(1 - epsilon, y_pred[i]))
        
        entropy = -(y_true[i] * math.log(y_pred_clipped) + 
                   (1 - y_true[i]) * math.log(1 - y_pred_clipped))
        sum_entropy += entropy
    
    bce = sum_entropy / n
    return bce


def normalize_to_probability(values):
    min_val = min(values)
    max_val = max(values)
    
    if min_val == max_val:
        return [0.5] * len(values)
    
    normalized = [(v - min_val) / (max_val - min_val) for v in values]
    return normalized

print("=" * 70)
print("LOSS FUNCTIONS DEMONSTRATION")
print("=" * 70)

# Sample Data for Regression (MSE)
y_true = [10, 20, 30]
y_pred = [12, 18, 33]

print("\n1. MEAN SQUARED ERROR (MSE) - For REGRESSION")
print("-" * 70)
print(f"Actual values (y_true):    {y_true}")
print(f"Predicted values (y_pred): {y_pred}")

# Calculate MSE manually
mse_value = calculate_mse(y_true, y_pred)
print(f"\nCalculation:")
for i in range(len(y_true)):
    error = y_true[i] - y_pred[i]
    squared_error = error ** 2
    print(f"  Sample {i+1}: ({y_true[i]} - {y_pred[i]})² = ({error})² = {squared_error}")

print(f"\nMSE = (1/{len(y_true)}) * sum of squared errors")
print(f"MSE = (1/{len(y_true)}) * {sum([(y_true[i] - y_pred[i])**2 for i in range(len(y_true))])}")
print(f"\n✓ Mean Squared Error (MSE): {mse_value:.4f}")

# Sample Data for Classification (BCE)
print("\n" + "=" * 70)
print("2. BINARY CROSS ENTROPY (BCE) - For CLASSIFICATION")
print("-" * 70)

# For BCE, we need probability values (0-1)
y_true_classification = [0, 1, 1]  # Binary labels (0 or 1)
y_pred_classification = [0.1, 0.8, 0.9]  # Predicted probabilities

print(f"Actual labels (y_true):        {y_true_classification}")
print(f"Predicted probabilities (y_pred): {y_pred_classification}")

# Calculate BCE
bce_value = calculate_binary_cross_entropy(y_true_classification, y_pred_classification)
print(f"\nCalculation:")
print(f"BCE = -(1/n) * Σ[y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred)]")
print()

for i in range(len(y_true_classification)):
    term1 = y_true_classification[i] * math.log(y_pred_classification[i])
    term2 = (1 - y_true_classification[i]) * math.log(1 - y_pred_classification[i])
    entropy = -(term1 + term2)
    print(f"  Sample {i+1}: -[{y_true_classification[i]} * ln({y_pred_classification[i]}) + "
          f"{1-y_true_classification[i]} * ln({1-y_pred_classification[i]})]")
    print(f"          = -[{term1:.6f} + {term2:.6f}] = {entropy:.6f}")

print(f"\n✓ Binary Cross Entropy (BCE): {bce_value:.4f}")

# Example: Using original data with BCE (normalized to probabilities)
print("\n" + "=" * 70)
print("3. BCE with NORMALIZED original data (alternative approach)")
print("-" * 70)
print(f"Original actual values:    {y_true}")
print(f"Original predicted values: {y_pred}")

y_true_normalized = normalize_to_probability(y_true)
y_pred_normalized = normalize_to_probability(y_pred)

print(f"\nNormalized actual values (0-1):    {[f'{v:.4f}' for v in y_true_normalized]}")
print(f"Normalized predicted values (0-1): {[f'{v:.4f}' for v in y_pred_normalized]}")

bce_normalized = calculate_binary_cross_entropy(y_true_normalized, y_pred_normalized)
print(f"\n✓ Binary Cross Entropy (normalized): {bce_normalized:.4f}")

# Summary
print("\n" + "=" * 70)
print("SUMMARY & EXPLANATION")
print("=" * 70)
print("""
┌─────────────────────────────────────────────────────────────────────┐
│ WHEN TO USE EACH LOSS FUNCTION:                                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ 1. MEAN SQUARED ERROR (MSE):                                       │
│    • Used for: REGRESSION problems                                │
│    • Problem type: Predicting continuous values                   │
│    • Examples: Price prediction, temperature forecasting          │
│    • Output range: Any real number                                │
│    • Advantage: Simple, interpretable, penalizes large errors    │
│                                                                     │
│ 2. BINARY CROSS ENTROPY (BCE):                                     │
│    • Used for: BINARY CLASSIFICATION problems                     │
│    • Problem type: Yes/No, True/False, 0/1 predictions           │
│    • Examples: Email spam detection, disease diagnosis            │
│    • Output range: Probabilities (0-1)                           │
│    • Advantage: Works well with probability distributions         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
""")
