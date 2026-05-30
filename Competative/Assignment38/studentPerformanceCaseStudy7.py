import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
stHour = np.array(df["StudyHours"])
prvScore = np.array(df["PreviousScore"])
plt.figure(figsize=(7,5))
plt.scatter(stHour, prvScore)
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Scatter Plot of Study Hours vs Previous Score")
plt.grid(True)
plt.show()