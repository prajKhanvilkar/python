import pandas as pd 

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
print("Total number of students")
print(df.shape[0])
print("Count how many number of students passed (FinalResult ==1)")
count_1 = (df["FinalResult"] == 1).sum()
print(count_1)
print("Count how many number of students Failed (FinalResult ==0)")
count_0 = (df["FinalResult"] == 0).sum()
print(count_0)