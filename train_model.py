import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

def train_and_save(output_model):
    # Load dataset
    df = pd.read_csv("dreams.csv")
    texts = df["dream_text"]
    labels = df["theme"]

    # Split without stratify (since small dataset)
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=42)

    # Use TF-IDF instead of CountVectorizer for better generalization
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2), min_df=1)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Use Logistic Regression instead of Naive Bayes (works better with small data)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    # Evaluate
    preds = model.predict(X_test_vec)
    print("\n--- Training Results ---")
    print("Accuracy:", accuracy_score(y_test, preds))
    print("\nClassification Report:\n", classification_report(y_test, preds, zero_division=0))

    # Save model + vectorizer
    joblib.dump({"model": model, "vectorizer": vectorizer}, output_model)
    print(f"\nModel saved to {output_model}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    train_and_save(args.output)


