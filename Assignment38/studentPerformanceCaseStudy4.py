import pandas as pd 

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
counts = df["FinalResult"].value_counts()
percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("Counts:\n", counts)
print("\nPercentage:\n", percentage)
print("The data is Balanced")