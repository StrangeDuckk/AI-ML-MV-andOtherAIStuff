# Rozpoznawanie obrazów – CIFAR-10 (CNN)
Deep Learning | Convolutional Neural Networks | Keras / TensorFlow

Projekt przedstawia implementację oraz trening konwolucyjnej sieci neuronowej (CNN) do klasyfikacji obrazów ze zbioru CIFAR-10.
---

## 📌 Cele projektu

- zbudowanie i wytrenowanie modelu CNN od podstaw
- zrozumienie działania warstw konwolucyjnych
- analiza wpływu technik regularyzacji
- wizualizacja procesu uczenia
- ocena jakości klasyfikacji obrazów

---
## 📊 Dane – CIFAR-10
- 📦 Dataset: CIFAR-10
- 🖼️ Obrazy: 32×32 RGB
- 🔢 Liczba klas: 10

---
## Klasy:
    - airplane ✈️
    - automobile 🚗
    - bird 🐦
    - cat 🐱
    - deer 🦌
    - dog 🐶
    - frog 🐸
    - horse 🐴
    - ship 🚢
    - truck 🚚

---
## ⚙️ Preprocessing danych
- Normalizacja pikseli:

        [0–255] → [0–1]
- One-hot encoding etykiet
- Podział na:
  - zbiór treningowy
  - zbiór testowy

---
## 🏗️ Architektura modelu

Model oparty o Convolutional Neural Network (CNN):

🔹 Blok 1
- Conv2D (32 filtry)
- Batch Normalization
- ReLU
- MaxPooling
- Dropout (0.1)

🔹 Blok 2
- Conv2D (64 filtry)
- Batch Normalization
- ReLU
- MaxPooling
- Dropout (0.2)

🔹 Klasyfikator (Dense)
- Flatten
- Dense (128)
- Batch Normalization
- ReLU
- Dropout (0.5)
- Dense (10, softmax)

---
## 🧠 Kluczowe komponenty
🔸 Convolution (Conv2D)
- wykrywanie cech: krawędzie, tekstury, kształty

🔸 Batch Normalization
- stabilizacja treningu
- szybsza konwergencja

🔸 Dropout
- redukcja overfittingu
- losowe „wyłączanie” neuronów

🔸 Softmax
- zwraca prawdopodobieństwo przynależności do klas

---
## ⚡ Trenowanie
- Optymalizator: Adam (learning_rate = 1e-3)
- Funkcja straty: categorical_crossentropy
- Batch size: 64
- Maksymalnie: 50 epok
## 🔄 Callbacki:
- EarlyStopping
  - zatrzymuje trening przy braku poprawy
- ReduceLROnPlateau
  - zmniejsza learning rate gdy model się „zatrzyma”
---
## 📈 Ewaluacja

Model oceniany na zbiorze testowym:
- Accuracy
- Loss

wykresy:
- loss (train vs validation)
- accuracy (train vs validation)

---
## 🔍 Analiza wyników
### 📊 Wizualizacje:
- przebieg uczenia (loss / accuracy)
- przykłady błędnych klasyfikacji
- macierz pomyłek (confusion matrix)
### 📌 Interpretacja:
- model dobrze rozpoznaje wyraźne obiekty (np. samochody, statki)
- trudności przy podobnych klasach (np. kot vs pies)
### 🧾 Struktura kodu
- import i przygotowanie danych (cifar10)
- preprocessing (normalizacja + one-hot)
- budowa modelu (Sequential)
- trening (fit)
- ewaluacja (evaluate)
- wizualizacje (matplotlib)
- analiza błędów + confusion matrix