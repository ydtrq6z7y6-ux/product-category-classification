import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


# 1. Učitavanje podataka
df = pd.read_csv("data/IMLP6_TASK_03-products.csv")

# 2. Standardizacija naziva stupaca
df.columns = df.columns.str.strip()

# 3. Čišćenje podataka
df_clean = df.dropna(
    subset=["Product Title", "Category Label"]
).copy()

# 4. Standardizacija kategorija
df_clean["Category Label"] = (
    df_clean["Category Label"]
    .astype(str)
    .str.strip()
)

category_mapping = {
    "Fridge": "Fridges",
    "fridge": "Fridges",
    "Freezer": "Freezers",
    "freezer": "Freezers",
    "Fridge Freezer": "Fridge Freezers",
    "fridge freezer": "Fridge Freezers",
}

df_clean["Category Label"] = (
    df_clean["Category Label"]
    .replace(category_mapping)
)

# 5. Ulazni podaci i ciljna varijabla
X = df_clean["Product Title"].astype(str)
y = df_clean["Category Label"]

# 6. Podjela na trening i test skup
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 7. TF-IDF
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 8. Treniranje najboljeg modela
model = LinearSVC()

model.fit(X_train_tfidf, y_train)

# 9. Provjera točnosti
y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print(f"Linear SVM accuracy: {accuracy:.4f}")

# 10. Spremanje modela i TF-IDF vektorizatora
joblib.dump(model, "model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("Model spremljen kao model.joblib")
print("TF-IDF vektorizator spremljen kao vectorizer.joblib")