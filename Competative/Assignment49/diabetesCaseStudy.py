import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import VotingClassifier
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler

def marvellousDitector(file):
    border = "-" * 40
    print(border)
    print("Load the Dataset")
    data = pd.read_csv(file)

    print("Size of dataset")
    print(data.shape)
    print("First five records are")
    print(data.head())
    print("Basic information about dataset")
    print(data.describe())
    print(border)
    print("Visualization of Distribution of target variable")
    plt.hist(data["Outcome"], bins=2)
    plt.xlabel("Outcome")
    plt.ylabel("Frequency")
    plt.title("Distribution of Diabetes Outcome")
    plt.show()
    print(border)
    print("Check for missing values")
    print(data.isnull().sum())
    print(border)
    print("Split the data into features and target variable")
    X = data.drop(columns="Outcome")
    Y = data["Outcome"]

    print("Shape of X:", X.shape)
    print("Shape of Y:", Y.shape)
    print(border)
    print("Scale the features")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Shape of X_scaled:", X_scaled.shape)
    print(border)
    print("Split the data into training and testing sets")
    X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

    print("Shape of X_train:", X_train.shape)
    print("Shape of X_test:", X_test.shape)
    print("Shape of Y_train:", Y_train.shape)
    print("Shape of Y_test:", Y_test.shape)
    print(border)
    print("Train the models")

    model_lr = LogisticRegression(max_iter=5000)
    model_dt = DecisionTreeClassifier(random_state=42)
    model_knn = KNeighborsClassifier(n_neighbors=5)

    model_lr.fit(X_train,Y_train)
    model_dt.fit(X_train,Y_train)
    model_knn.fit(X_train,Y_train)

    soft_model = VotingClassifier(
        estimators= [('lr',model_lr),('dt',model_dt),('knn',model_knn)],
        voting="soft"
    )
    soft_model.fit(X_train,Y_train)
    print("Evaluate the model")
    pred_soft = soft_model.predict(X_test)

    acc_soft = accuracy_score(pred_soft,Y_test)
    print("Accuracy is", acc_soft*100)

    cm  = confusion_matrix(pred_soft,Y_test)
    print("Confusion matrix\n:",cm)
    print(border)
    print("Plot the confusion matrix")  
    plt.figure(figsize=(6,4))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.colorbar()
    tick_marks = range(len(set(Y)))
    plt.xticks(tick_marks, tick_marks)
    plt.yticks(tick_marks, tick_marks)
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.show()

    cr = classification_report(pred_soft,Y_test)
    print("Classification report \n",cr)


def main():
    border = "-" * 40
    print(border)
    print("Diabetes Classifier Using Unsable ML")
    print(border)
    marvellousDitector('diabetes.csv')

if __name__ == "__main__":
    main()