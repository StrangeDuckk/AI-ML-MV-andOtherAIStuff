# Klasyfikacja danych – porównanie modeli ML
Logistic Regression, Decision Trees, Random Forest, SVM & Ensemble

Projekt przedstawia kompleksowe porównanie różnych metod 
klasyfikacji binarnej na syntetycznym zbiorze danych, 
wraz z wizualizacją granic decyzyjnych oraz analizą jakości modeli.

---

## 📌 Cele projektu

- implementacja własnego modelu regresji logistycznej
- porównanie go z popularnymi algorytmami ML
- analiza wpływu parametrów modeli na jakość klasyfikacji
- wizualizacja decision boundary
- zrozumienie różnic między podejściami probabilistycznymi i geometrycznymi

---
## 📊 Dane
- Dataset: make_moons
- Liczba próbek: 10 000
- Szum: 0.25
- Standaryzacja: 
- Podział:
  - 80% trening
  - 20% test

Zbiór jest nieliniowo separowalny, co stanowi dobre środowisko testowe dla modeli.

---

## 🧠 Zaimplementowane modele

1. Regresja logistyczna (własna implementacja)
   - Implementacja od podstaw (bez sklearn)
   - Funkcja sigmoidalna
   - Zwraca prawdopodobieństwa klas
   - Uczenie na podstawie danych treningowych 
   - 📌 Kluczowa różnica vs perceptron:
     - sigmoid vs funkcja progowa 
     - probabilistyczne wyjście zamiast binarnego
 
2. Drzewo decyzyjne 
   - DecisionTreeClassifier
   - Testowane parametry:
     - kryterium: gini vs entropy
     - głębokość drzewa
   - 📌 Wnioski:
     - większa głębokość → lepsze dopasowanie, ale ryzyko overfittingu 
     - Gini → szybsze 
     - Entropy → bardziej informacyjne podziały
3. Random Forest 🌲 
   - Ensemble wielu drzew decyzyjnych
   - Testowana liczba drzew (n_estimators)
   - 📌 Zalety:
     - redukcja overfittingu
     - większa stabilność
     - lepsza generalizacja
4. Support Vector Machine (SVM)
   - Kernel:
   - liniowy
   - RBF (nieliniowy)
   - 📌 Idea:
     - maksymalizacja marginesu między klasami
     - kernel trick pozwala modelować nieliniowe granice
5. Ensemble – Voting Classifier 🗳️
   - Połączenie modeli:
     - SVM
     - Logistic Regression
     - Random Forest
   - 📌 Strategie:
     - Hard voting – głosowanie większościowe
     - Soft voting – średnia prawdopodobieństw
   - 📌 Zaleta:
     - redukcja błędów pojedynczych modeli
     - lepsza stabilność predykcji

---

## 📈 Wizualizacja

Każdy model prezentowany jest za pomocą:

- decision boundary
- danych treningowych i testowych
- metryk:
  - accuracy (train/test)
  - precision (opcjonalnie)

---
## 📊 Ewaluacja modeli

Porównanie obejmuje:

- Logistic Regression (custom)
- Decision Tree (Gini / Entropy)
- Random Forest
- SVM
- Voting Classifier

📌 Metryka:
- Accuracy

📌 Dodatkowo:
- wizualna analiza granic decyzyjnych

---

## ⚙️ Struktura kodu
- *plot_decision_boundary_with_metrics* – wizualizacja + metryki
- generowanie danych (make_moons)
- preprocessing (StandardScaler)
- implementacja własna (reglog.py)
- modele sklearn
- ewaluacja i porównanie

---

## Pytania do projektu:

- Perceptron vs Logistic Regression 
  - deterministyczny vs probabilistyczny model 
  - brak vs obecność funkcji sigmoidalnej
- OvR vs OvO
  - OvR: mniej modeli, szybsze 
  - OvO: dokładniejsze, ale kosztowne
- Entropy vs Gini
  - entropy: bardziej informacyjne 
  - gini: szybsze obliczeniowo
- Random Forest
  - redukcja wariancji przez losowość i ensemble
- SVM
  - maksymalny margines 
  - kernel trick dla nieliniowości
- Voting Classifier
  - łączenie modeli → lepsza generalizacja