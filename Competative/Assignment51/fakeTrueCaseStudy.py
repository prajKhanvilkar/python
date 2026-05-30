# Import required libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def main():

    # -------------------------------
    # Part 1: Load and Prepare Data
    # -------------------------------

    # Load datasets
    fake_df = pd.read_csv("Fake.csv")
    true_df = pd.read_csv("True.csv")

    # Add labels
    fake_df["label"] = 0   # Fake
    true_df["label"] = 1   # Real

    # Combine datasets
    df = pd.concat([fake_df, true_df], axis=0)

    # Shuffle dataset
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Keep only useful columns (using 'text')
    df = df[['text', 'label']]

    # Drop null values
    df.dropna(inplace=True)

    print("Dataset shape:", df.shape)

    # -------------------------------
    # Part 2: Feature Extraction
    # -------------------------------

    # TF-IDF Vectorization
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)

    X = tfidf.fit_transform(df['text'])
    y = df['label']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------------
    # Part 3: Model Training
    # -------------------------------

    # Individual models
    lr = LogisticRegression(max_iter=1000)
    dt = DecisionTreeClassifier()

    # Train models
    lr.fit(X_train, y_train)
    dt.fit(X_train, y_train)

    # Predictions
    lr_pred = lr.predict(X_test)
    dt_pred = dt.predict(X_test)

    # -------------------------------
    # Voting Classifier
    # -------------------------------

    # Hard Voting
    voting_hard = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='hard'
    )

    voting_hard.fit(X_train, y_train)
    hard_pred = voting_hard.predict(X_test)

    # Soft Voting
    voting_soft = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='soft'
    )

    voting_soft.fit(X_train, y_train)
    soft_pred = voting_soft.predict(X_test)

    # -------------------------------
    # Part 4: Evaluation
    # -------------------------------

    def evaluate_model(name, y_true, y_pred):
        print(f"\n{name} Results:")
        print("Accuracy:", accuracy_score(y_true, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
        print("Classification Report:\n", classification_report(y_true, y_pred))

    # Evaluate all models
    evaluate_model("Logistic Regression", y_test, lr_pred)
    evaluate_model("Decision Tree", y_test, dt_pred)
    evaluate_model("Hard Voting", y_test, hard_pred)
    evaluate_model("Soft Voting", y_test, soft_pred)

if __name__ == "__main__":
    main()