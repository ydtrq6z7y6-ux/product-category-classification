# Product Category Classification

## Opis projekta

Projekt se bavi automatskom klasifikacijom proizvoda u odgovarajuće kategorije na temelju naziva proizvoda.

Za pretvaranje tekstualnih podataka u numerički oblik korišten je TF-IDF, a testirana su tri klasifikacijska modela:

- Logistic Regression
- Linear SVM
- Naive Bayes

Cilj projekta je pronaći model koji može što preciznije predvidjeti kategoriju proizvoda na temelju njegovog naziva.

## Podaci

Korišten je dataset koji sadrži 35.096 proizvoda raspoređenih u 10 standardiziranih kategorija.

Dataset se nalazi u:

data/IMLP6_TASK_03-products.csv

## Korištene tehnologije

- Python
- Pandas
- Scikit-learn
- Joblib
- Matplotlib
- Seaborn
- Jupyter Notebook
- TF-IDF
- Linear SVM

## Rezultati modela

Testirana su tri klasifikacijska modela:

| Model | Accuracy |
|---|---:|
| Logistic Regression | 95.61% |
| Linear SVM | 96.50% |
| Naive Bayes | 94.86% |

Najbolji rezultat u Jupyter Notebook analizi ostvario je Linear SVM s točnošću od 96.50%.

Završna skripta za treniranje modela ostvaruje accuracy od 95.84%.

## Struktura projekta

product-category-classification/

├── data/

│   └── IMLP6_TASK_03-products.csv

├── notebooks/

│   └── product_category_classification.ipynb

├── train_model.py

├── predict_category.py

├── model.pkl

├── vectorizer.pkl

└── README.md

## Analiza podataka

U početnoj fazi učitani su podaci i provedeno je čišćenje podataka.

Provjereni su nazivi stupaca, nedostajuće vrijednosti i struktura dataseta.

Nakon čišćenja dataset sadrži 35.096 proizvoda.

## TF-IDF vektorizacija

Budući da su ulazni podaci tekstualni, nazivi proizvoda pretvoreni su u numerički oblik pomoću TF-IDF vektorizacije.

TF-IDF omogućuje modelu da prepozna važne riječi i izraze u nazivima proizvoda.

## Treniranje modela

Podaci su podijeljeni na trening i test skup.

Za završni model korišten je Linear SVM.

Model se trenira pomoću skripte:

python train_model.py

Nakon treniranja stvaraju se:

- model.pkl
- vectorizer.pkl

## Evaluacija

Linear SVM je u završnoj skripti ostvario accuracy od 95.84%.

Model je uspješno testiran na novim nazivima proizvoda.

Primjer:

samsung galaxy s24 256gb

Predviđena kategorija: Mobile Phones

## Pokretanje projekta

### Instalacija potrebnih biblioteka

U terminalu instalirati potrebne biblioteke:

pip install pandas scikit-learn joblib matplotlib seaborn

### Treniranje modela

Pokrenuti:

python train_model.py

### Interaktivno testiranje

Pokrenuti:

python predict_category.py

Program omogućuje unos naziva proizvoda i vraća predviđenu kategoriju.

Za završetak programa upisati:

exit

## Jupyter Notebook

Kompletna analiza i razvoj modela prikazani su u:

notebooks/product_category_classification.ipynb

Notebook sadrži:

- učitavanje podataka
- čišćenje podataka
- pripremu tekstualnih podataka
- TF-IDF vektorizaciju
- podjelu podataka na trening i test skup
- treniranje više modela
- evaluaciju modela
- usporedbu rezultata
- confusion matrix
- odabir najboljeg modela

## Zaključak

U projektu je razvijen model za automatsku klasifikaciju proizvoda prema njihovom nazivu.

U Jupyter Notebook analizi najbolji rezultat ostvario je Linear SVM s accuracy rezultatom od 96.50%.

Završna skripta za treniranje uspješno trenira Linear SVM i sprema model u model.pkl te TF-IDF vektorizator u vectorizer.pkl.

Skripta predict_category.py omogućuje interaktivno predviđanje kategorije novih proizvoda.

Projekt je organiziran tako da drugi član tima može pregledati analizu, ponovno trenirati model i koristiti ga za klasifikaciju novih proizvoda.