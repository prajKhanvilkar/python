import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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
# Step4 : Create Random Forest Model
#--------------------------------------------------------------------
rf_model = RandomForestClassifier(
              n_estimators=100,
               random_state=42
            )

#--------------------------------------------------------------------
# Step5 : Train  Model
#--------------------------------------------------------------------

rf_model.fit(X_train,Y_train)

#--------------------------------------------------------------------
# Step6 : Test  Model
#--------------------------------------------------------------------

Y_pred = rf_model.predict(X_test)

#--------------------------------------------------------------------
# Step7 : Accuracy Score  Model
#--------------------------------------------------------------------
accuracy = accuracy_score(Y_test,Y_pred)

print("accuracy Score\n",accuracy)


#--------------------------------------------------------------------
# Step8 : Confusion Matrix  Model
#--------------------------------------------------------------------
cm = confusion_matrix(Y_test,Y_pred)

print("Confustion Matrix  \n",cm)

#--------------------------------------------------------------------
# Step9 : Classification Report  Model
#--------------------------------------------------------------------
cf = classification_report(Y_test,Y_pred)

print("Classification report  \n",cf)

