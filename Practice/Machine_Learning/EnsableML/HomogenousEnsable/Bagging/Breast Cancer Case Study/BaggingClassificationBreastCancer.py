import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#----------------------------------------------------------------------
# Step1 : Load Dataset
#---------------------------------------------------------------------
df = pd.read_csv("breast_cancer.csv")
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
base_model = DecisionTreeClassifier(random_state=42)

#--------------------------------------------------------------------
# Step5 : Create Bagging Model
#--------------------------------------------------------------------

bagging_model = BaggingClassifier(
    estimator=base_model,
    n_estimators=10,
    random_state=42
)

#--------------------------------------------------------------------
# Step6 : Train Bagging Model
#--------------------------------------------------------------------

bagging_model.fit(X_train,Y_train)

#--------------------------------------------------------------------
# Step7 : Test Bagging Model
#--------------------------------------------------------------------

Y_pred = bagging_model.predict(X_test)

#--------------------------------------------------------------------
# Step8 : Accuracy Score Bagging Model
#--------------------------------------------------------------------
accuracy = accuracy_score(Y_test,Y_pred)

print("accuracy Score\n",accuracy)


#--------------------------------------------------------------------
# Step8 : Confusion Matrix Bagging Model
#--------------------------------------------------------------------
cm = confusion_matrix(Y_test,Y_pred)

print("Confustion Matrix  \n",cm)

#--------------------------------------------------------------------
# Step9 : Classification Report Bagging Model
#--------------------------------------------------------------------
cf = classification_report(Y_test,Y_pred)

print("Classification report  \n",cf)

