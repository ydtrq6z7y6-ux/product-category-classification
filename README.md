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

Najbolji rezultat ostvario je Linear SVM s točnošću od 96.50%.

Na temelju rezultata Linear SVM odabran je kao završni model za klasifikaciju novih proizvoda.

## Struktura projekta

product-category-classification/

├── data/

│   └── IMLP6_TASK_03-products.csv

├── notebooks/

│   └── product_category_classification.ipynb

├── train_model.py

├── predict_category.py

├── model.joblib

├── vectorizer.joblib

└── README.md

## Analiza podataka

U početnoj fazi učitani su podaci i provedeno je čišćenje podataka.

Provjereni su nazivi stupaca, nedostajuće vrijednosti i struktura dataseta.

Nakon čišćenja dataset je korišten za treniranje klasifikacijskih modela.

## TF-IDF vektorizacija

Budući da su ulazni podaci tekstualni, nazivi proizvoda pretvoreni su u numerički oblik pomoću TF-IDF vektorizacije.

TF-IDF omogućuje modelu da prepozna važne riječi i izraze u nazivima proizvoda.

## Treniranje modela

Podaci su podijeljeni na trening i test skup.

Testirana su tri modela:

- Logistic Regression
- Linear SVM
- Naive Bayes

Svaki model je evaluiran pomoću accuracy metrike i classification reporta.

## Evaluacija

Linear SVM ostvario je najbolji rezultat:

Accuracy: 96.50%

Confusion matrix pokazuje da model vrlo dobro razlikuje većinu kategorija.

Najviše pogrešaka pojavljuje se između međusobno sličnih kategorija, posebno između:

- Fridges
- Freezers
- Fridge Freezers

To je očekivano jer se radi o semantički sličnim kategorijama proizvoda.

## Pokretanje projekta

### 1. Instalacija potrebnih biblioteka

U terminalu instalirati potrebne biblioteke:

pip install pandas scikit-learn joblib matplotlib seaborn

### 2. Treniranje modela

Za treniranje modela pokrenuti:

python train_model.py

Skripta trenira Linear SVM model i sprema:

- model.joblib
- vectorizer.joblib

### 3. Interaktivno testiranje modela

Za testiranje modela pokrenuti:

python predict_category.py

Program omogućuje unos naziva proizvoda i vraća predviđenu kategoriju.

Primjer:

Naziv proizvoda: samsung galaxy s24 256gb

Predviđena kategorija: Mobile Phones

Za završetak programa upisati:

exit

## Jupyter Notebook

Kompletna analiza i razvoj modela prikazani su u Jupyter Notebooku:

notebooks/product_category_classification.ipynb

Notebook sadrži:

- učitavanje podataka
- čišćenje podataka
- pripremu tekstualnih podataka
- TF-IDF vektorizaciju
- podjelu podataka na trening i test skup
- treniranje modela
- evaluaciju modela
- usporedbu rezultata
- prikaz confusion matrixa
- odabir najboljeg modela

## Zaključak

U projektu je razvijen model za automatsku klasifikaciju proizvoda prema njihovom nazivu.

Od tri testirana modela najbolji rezultat ostvario je Linear SVM s točnošću od 96.50%.

Model je spremljen u datoteku model.joblib, dok je TF-IDF vektorizator spremljen u vectorizer.joblib.

Pomoću skripte predict_category.py moguće je interaktivno unositi nove proizvode i dobiti njihovu predviđenu kategoriju.

Projekt je organiziran tako da se analiza može pregledati kroz Jupyter Notebook, model ponovno trenirati pomoću train_model.py, a gotov model testirati pomoću predict_category.py.