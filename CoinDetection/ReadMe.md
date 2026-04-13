# Detekcja monet na obrazach
Computer Vision | OpenCV | Hough Transform

Projekt przedstawia system do automatycznego wykrywania monet na obrazach oraz określania ich wartości i położenia względem tacki.

---
## 📌 Cel projektu
- wykrycie monet na obrazach
- określenie ich nominałów na podstawie rozmiaru
- rozróżnienie monet:
  - 🟢 na tacce
  - 🔴 poza tacką
- obliczenie wartości monet
- oszacowanie pola tacki w cm²

---

## 📊 Dane wejściowe
- Zestaw obrazów: tray1.jpg – tray8.jpg
- Obrazy w skali szarości
- Monety o różnych rozmiarach

---

## ⚙️ Pipeline przetwarzania
1️⃣ Wczytanie danych
- Obrazy wczytywane jako grayscale (cv2.imread)
- Wizualizacja danych wejściowych

2️⃣ Odszumianie i detekcja krawędzi
Zastosowane operatory:
- Sobel (krawędzie poziome i pionowe)
- Laplacian (detekcja zmian intensywności)
📌 Cel:
- uwydatnienie krawędzi
- przygotowanie do dalszej analizy

3️⃣ Detekcja tacki (konturu)
Pipeline:
- Gaussian Blur (redukcja szumu)
- Canny Edge Detection
- Transformata Hougha (cv2.HoughLines)

🔍 Dodatkowe kroki:
- podział linii na:
  - pionowe
  - poziome
-  grupowanie podobnych linii
-  uśrednianie parametrów (rho, theta)
-  wyznaczenie 4 krawędzi tacki

📐 Wyznaczenie rogów:
-  przecięcia linii → kontur tacki

---
## Detekcja monet
Wykorzystano:
- cv2.HoughCircles

Parametry:
- detekcja okręgów na rozmytym obrazie
- ograniczenie promienia (min/max radius)

Wynik:
- pozycja (x, y)
- promień r

---

## 💰 Klasyfikacja monet (nominały)
- monety klasyfikowane na podstawie rozmiaru (promienia)
- największe → przypisywana wyższa wartość

📌 Przykład:
- 2 największe monety → wartość = 5
- pozostałe → wartość = 0.05

---
## 📍 Analiza położenia monet

Dla każdej monety:
- sprawdzenie czy znajduje się w konturze tacki:

    
    cv2.pointPolygonTest()
Wynik:
- 🟢 moneta na tacce
- 🔴 moneta poza tacką

---

## 📏 Skalowanie i obliczenia
🔹 Kalibracja skali
- największa moneta używana jako odniesienie:

    
    2.4 cm = średnica największej monety
🔹 Obliczenia:
- pole tacki:
    - w pikselach
    - przeliczone na cm²
- suma wartości monet:
  - na tacce
  - poza tacką

---
## 📈 Wizualizacja

Projekt generuje:

- obrazy z wykrytymi:
    - krawędziami
    - liniami tacki
    - monetami
- oznaczenia:
    - 🟢 na tacce
    - 🔴 poza tacką
---

## 🧾 Struktura kodu
- wczytywanie danych
- preprocessing (filtry + krawędzie)
- detekcja tacki (Hough Lines)
- detekcja monet (Hough Circles)
- klasyfikacja monet
- analiza położenia
- obliczenia i wizualizacja