import pandas as pd 

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
print("First five records:")
print(df.head())
print("Last five records:")
print(df.tail())
print("Total numbers of rows and columns")
print(df.shape)
print("list of column")
print(list(df.columns))
print("Data Types of each column")
print(list(df.dtypes))