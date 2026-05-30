from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import VotingClassifier

#step 1: Load dataset
data = load_breast_cancer()
X = data.data
Y = data.target

print("Shape of X:", X.shape)
print("Shape of Y:", Y.shape)

#step 2: Split the data set
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of Y_train:", Y_train.shape)
print("Shape of Y_test:", Y_test.shape)

#step3: create Base Models

model_lr = LogisticRegression(max_iter=5000)
model_dt = DecisionTreeClassifier(random_state=42)
model_knn = KNeighborsClassifier(n_neighbors=5)

#step 4: tain the base models
model_lr.fit(X_train,Y_train)
model_dt.fit(X_train,Y_train)
model_knn.fit(X_train,Y_train)

#step 5: Calculate Individual Accuracy
pred_lr = model_lr.predict(X_test)
pred_dt = model_dt.predict(X_test)
pred_knn = model_knn.predict(X_test)

acc_lr = accuracy_score(pred_lr,Y_test)
acc_dt = accuracy_score(pred_dt,Y_test)
acc_knn = accuracy_score(pred_knn,Y_test)
print("Accuracy of individual model\n")
print("Logistic Regression", acc_lr *100)
print("Decission Tree", acc_dt *100)
print("KNN", acc_knn * 100)

