import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

border = "-"*50
print(border)
DataSet = "student_performance_ml.csv"
df = pd.read_csv(DataSet)

sns.histplot(df["StudyHours"])
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Histogram of Study Hours")
plt.show()