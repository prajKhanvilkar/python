import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score
#----------------------------------------------------------------------
# Step1 : Load Dataset
#---------------------------------------------------------------------
df = pd.read_csv("california_housing.csv")
print("Shape od Dataset:", df.shape)
print("First 5 records: ",df.head())

#--------------------------------------------------------------------
# Step2 : seperate features and lables 
#--------------------------------------------------------------------
X = df.drop("target",axis=1)
Y = df["target"]

#--------------------------------------------------------------------
# Step3 : Split Dataset for training and testing
#--------------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#--------------------------------------------------------------------
# Step4 : Create Base Model
#--------------------------------------------------------------------
model = DecisionTreeRegressor(random_state=42)

#--------------------------------------------------------------------
# Step5 : Train Bagging Model
#--------------------------------------------------------------------

model.fit(X_train,Y_train)

#--------------------------------------------------------------------
# Step6 : Test Bagging Model
#--------------------------------------------------------------------

Y_pred = model.predict(X_test)

#--------------------------------------------------------------------
# Step7 : Evaluate  Bagging Model
#--------------------------------------------------------------------

print("Mean Squared Error \n",mean_squared_error(Y_test,Y_pred))

print("R Squared  \n",r2_score(Y_test,Y_pred))



