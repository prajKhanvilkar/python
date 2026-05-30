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

#step 5: soft Voting classification
soft_model = VotingClassifier(
    estimators= [('lr',model_lr),('dt',model_dt),('knn',model_knn)],
    voting="soft"
)
soft_model.fit(X_train,Y_train)
pred_soft = soft_model.predict(X_test)

acc_soft = accuracy_score(pred_soft,Y_test)
print("Accuracy is", acc_soft*100)

cm  = confusion_matrix(pred_soft,Y_test)
print("Confusion matrix\n:",cm)

cr = classification_report(pred_soft,Y_test)
print("Classification report \n",cr)
