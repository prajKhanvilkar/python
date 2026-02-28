import pandas as pd 

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
print("Average study Hours ")
print(df["StudyHours"].mean())
print("Average Attendence")
print(df["Attendance"].mean())
print("Maximum Previous Score")
print(df["PreviousScore"].max())
print("Minimum Sleep Hours")
print(df["SleepHours"].min())