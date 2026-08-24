import joblib

# Učitavanje treniranog modela i TF-IDF vektorizatora
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("Model za klasifikaciju proizvoda")
print("Upiši naziv proizvoda ili 'exit' za izlaz.\n")

while True:
    product_title = input("Naziv proizvoda: ")

    if product_title.lower() == "exit":
        print("Kraj programa.")
        break

    product_vector = vectorizer.transform([product_title])

    prediction = model.predict(product_vector)

    print(f"Predviđena kategorija: {prediction[0]}\n")