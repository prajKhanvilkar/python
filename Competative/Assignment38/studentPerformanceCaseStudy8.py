import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)
attendanceList = np.array(df["Attendance"])
sns.boxplot(x = list(df["Attendance"]))
plt.title("Box plot of attendance")
plt.show()