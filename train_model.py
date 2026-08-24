import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


# ============================================================
# 1. UČITAVANJE PODATAKA
# ============================================================

df = pd.read_csv("data/IMLP6_TASK_03-products.csv")

# Uklanjanje razmaka iz naziva stupaca
df.columns = df.columns.str.strip()

print("Stupci u datasetu:")
print(df.columns.tolist())

print(f"\nBroj redaka prije čišćenja: {len(df)}")


# ============================================================
# 2. ODABIR STUPACA
# ============================================================

title_column = "Product Title"
category_column = "Category Label"


# Provjera postoje li potrebni stupci
if title_column not in df.columns:
    raise ValueError(
        f"Nedostaje stupac '{title_column}'. "
        f"Dostupni stupci: {df.columns.tolist()}"
    )

if category_column not in df.columns:
    raise ValueError(
        f"Nedostaje stupac '{category_column}'. "
        f"Dostupni stupci: {df.columns.tolist()}"
    )


# ============================================================
# 3. ČIŠĆENJE PODATAKA
# ============================================================

df_clean = df.dropna(
    subset=[title_column, category_column]
).copy()

df_clean[title_column] = (
    df_clean[title_column]
    .astype(str)
    .str.strip()
)

df_clean[category_column] = (
    df_clean[category_column]
    .astype(str)
    .str.strip()
)

# Uklanjanje praznih vrijednosti
df_clean = df_clean[
    (df_clean[title_column] != "") &
    (df_clean[category_column] != "")
].copy()

print(f"Broj redaka nakon čišćenja: {len(df_clean)}")


# ============================================================
# 4. X I y
# ============================================================

X = df_clean[title_column]
y = df_clean[category_column]


# ============================================================
# 5. TRAIN / TEST PODJELA
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ============================================================
# 6. TF-IDF
# ============================================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.95
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# ============================================================
# 7. LINEAR SVM
# ============================================================

model = LinearSVC(
    random_state=42
)

model.fit(
    X_train_tfidf,
    y_train
)


# ============================================================
# 8. EVALUACIJA
# ============================================================

y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(f"\nLinear SVM accuracy: {accuracy:.4f}")


# ============================================================
# 9. Spremanje modela i TF-IDF vektorizatora
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel spremljen kao model.pkl")
print("TF-IDF vektorizator spremljen kao vectorizer.pkl")

print("\nTreniranje modela uspješno završeno.")