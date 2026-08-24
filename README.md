# Product Category Classification

## Opis projekta

Projekt se bavi automatskom klasifikacijom proizvoda u odgovarajuće kategorije na temelju naziva proizvoda.

Cilj projekta je razviti model mašinskog učenja koji može automatski predvidjeti kategoriju novog proizvoda na temelju njegovog naziva.

U projektu su testirana tri klasifikacijska modela:

- Logistic Regression
- Linear SVM
- Naive Bayes

Za pretvaranje tekstualnih podataka u numerički oblik korišten je TF-IDF.

## Podaci

Korišten je dataset s 35.311 proizvoda.

Nakon čišćenja podataka ostalo je 35.096 proizvoda.

Dataset se nalazi u `data/IMLP6_TASK_03-products.csv`.

Ciljna varijabla je `Category Label`, a ulazna varijabla je `Product Title`.

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

## Analiza i razvoj modela

U Jupyter Notebooku provedene su sljedeće faze:

- učitavanje podataka
- istraživanje strukture dataseta
- provjera nedostajućih vrijednosti
- čišćenje podataka
- analiza kategorija proizvoda
- analiza naziva proizvoda
- analiza duljine naziva i broja riječi
- TF-IDF vektorizacija
- podjela podataka na trening i test skup
- treniranje više klasifikacijskih modela
- evaluacija modela
- usporedba rezultata
- confusion matrix
- odabir najboljeg modela

## Rezultati modela

U eksperimentalnoj Jupyter Notebook analizi testirana su tri modela:

| Model | Accuracy |
| --- | ---: |
| Logistic Regression | 95.61% |
| Linear SVM | 96.50% |
| Naive Bayes | 94.86% |

Najbolji rezultat u eksperimentalnoj analizi ostvario je Linear SVM s accuracy rezultatom od 96.50%.

Nakon toga izrađena je završna verzija skripte za treniranje modela. Završni `train_model.py` ostvaruje accuracy od 95.84%.

Razlika u rezultatu posljedica je različitih postavki TF-IDF vektorizacije između eksperimentalnog notebooka i završne skripte.

## Završni model

Kao završni klasifikacijski algoritam koristi se Linear SVM.

Završna skripta `train_model.py` trenira model na podacima i sprema:

- `model.pkl`
- `vectorizer.pkl`

Model i vektorizator mogu se ponovno učitati bez ponovnog treniranja.

## Struktura projekta

- `data/` — dataset korišten za treniranje
- `notebooks/` — Jupyter Notebook s kompletnom analizom
- `train_model.py` — skripta za treniranje i spremanje modela
- `predict_category.py` — skripta za interaktivno predviđanje kategorije
- `model.pkl` — spremljeni Linear SVM model
- `vectorizer.pkl` — spremljeni TF-IDF vektorizator
- `.gitignore` — datoteke koje se ne spremaju u Git
- `README.md` — dokumentacija projekta

## Instalacija

Potrebno je imati instaliran Python.

Potrebne biblioteke:

- pandas
- scikit-learn
- joblib
- matplotlib
- seaborn

Biblioteke se mogu instalirati naredbom `pip install pandas scikit-learn joblib matplotlib seaborn`.

## Treniranje modela

Za treniranje završnog modela pokrenuti `python train_model.py`.

Skripta:

1. učitava dataset
2. čisti podatke
3. priprema tekstualne podatke
4. dijeli podatke na trening i test skup
5. primjenjuje TF-IDF
6. trenira Linear SVM
7. izračunava accuracy
8. sprema model u `model.pkl`
9. sprema TF-IDF vektorizator u `vectorizer.pkl`

Završna skripta ostvaruje accuracy od približno 95.84%.

## Interaktivno predviđanje

Za testiranje spremljenog modela pokrenuti `python predict_category.py`.

Program omogućuje unos naziva proizvoda i vraća predviđenu kategoriju.

Primjer:

**Unos:** samsung galaxy s24 256gb

**Predviđena kategorija:** Mobile Phones

Za završetak programa upisati `exit`.

## Jupyter Notebook

Kompletna analiza i razvoj modela nalaze se u `notebooks/product_category_classification.ipynb`.

Notebook prikazuje proces od istraživanja i čišćenja podataka do treniranja, evaluacije i usporedbe više modela.

## Evaluacija

Modeli su uspoređeni pomoću accuracy metrike, classification reporta i confusion matrixa.

Confusion matrix omogućuje pregled kategorija između kojih model najčešće griješi.

Veći broj pogrešaka očekivan je između semantički sličnih kategorija proizvoda.

## Zaključak

U projektu je razvijen sustav za automatsku klasifikaciju proizvoda prema njihovom nazivu.

Testirana su tri različita klasifikacijska algoritma, pri čemu je Linear SVM ostvario najbolji rezultat u eksperimentalnoj analizi.

Završna skripta `train_model.py` uspješno trenira Linear SVM model i sprema ga u `model.pkl`, zajedno s TF-IDF vektorizatorom u `vectorizer.pkl`.

Skripta `predict_category.py` omogućuje interaktivno predviđanje kategorije novih proizvoda.

Projekt je organiziran tako da drugi član tima može pregledati analizu, ponovno trenirati model ili koristiti postojeći model za klasifikaciju novih proizvoda.