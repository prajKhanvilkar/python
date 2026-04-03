import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)
def main():
    # 1. Load dataset
    df = pd.read_csv('bank-full.csv', sep=';')

    # Display basic info
    print("First 5 rows:\n", df.head())
    print("\nDataset Info:\n")
    print(df.info())
    print("\nBasic Stats:\n", df.describe())

    # 2. Handle missing / unknown values
    # Replace 'unknown'
    df.replace('unknown', np.nan, inplace=True)

    # Strip spaces
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Identify numeric columns FIRST
    for col in df.columns:
        # Try converting only if most values are numeric
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    # Handle missing values
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

    # 3. Visualize class distribution
    plt.figure()
    sns.countplot(x='y', data=df)
    plt.title("Class Distribution")
    plt.show()

    # 4. Encode target variable
    le = LabelEncoder()
    df['y'] = le.fit_transform(df['y'])  # yes=1, no=0

    # 5. Separate features and target
    X = df.drop('y', axis=1)
    y = df['y']

    # Identify categorical and numerical columns
    categorical_cols = X.select_dtypes(include=['object']).columns
    numerical_cols = X.select_dtypes(exclude=['object']).columns

    # 6. Preprocessing pipeline
    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(drop='first'), categorical_cols)
    ])

    # 7. Train-test split 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.8, random_state=42
    )

    # 8. Define models
    models = {
        "Decision Tree": DecisionTreeClassifier(),
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier()
    }

    # 9. Train, evaluate, and visualize
    for name, model in models.items():
        print(f"\n===== {name} =====")
        
        # Create pipeline
        pipe = Pipeline([
            ('preprocessing', preprocessor),
            ('model', model)
        ])
        
        # Train
        pipe.fit(X_train, y_train)
        
        # Predictions
        y_pred = pipe.predict(X_test)
        y_prob = pipe.predict_proba(X_test)[:, 1]
        
        # Metrics
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))
        print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))
        
        # 10. Plot Confusion Matrix
        plt.figure()
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d')
        plt.title(f"{name} - Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()
        
        # 11. Plot ROC Curve
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        
        plt.figure()
        plt.plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_test, y_prob):.2f}")
        plt.plot([0, 1], [0, 1], linestyle='--')
        plt.title(f"{name} - ROC Curve")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.legend()
        plt.show()

if __name__=="__main__":
    main()