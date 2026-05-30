import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
stHour = np.array(df["AssignmentsCompleted"])
prvScore = np.array(df["FinalResult"])
plt.figure(figsize=(7,5))
plt.scatter(stHour, prvScore)
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.title("Scatter Plot of Assignments Completed vs Final Result")
plt.grid(True)
plt.show()