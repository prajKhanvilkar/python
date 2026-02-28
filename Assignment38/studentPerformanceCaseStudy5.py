import pandas as pd 

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
print("Higher Study Hours increases the chance of paassing")
print(df.groupby("FinalResult")["StudyHours"].mean())
print(border)
print("correlation:")
print(df["StudyHours"].corr(df["FinalResult"]))
print(border)
print("Higher attendance improves final result")
print(df.groupby("FinalResult")["Attendance"].mean())
print(border)
print("correlation:")
print(df["Attendance"].corr(df["FinalResult"]))
print(border)
print(border)
print("Pass group has higher mean attendance")
print("Correlation is positive")
print("Pass rate increases across attendance ranges ")


