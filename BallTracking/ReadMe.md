# v🎯 Śledzenie obiektu w wideo (Ball Tracking)
Computer Vision, OpenCV, HSV Segmentation

Projekt przedstawia system do śledzenia obiektu (np. piłki) 
w obrazie i nagraniu wideo z wykorzystaniem filtracji koloru w przestrzeni HSV.

---

## 📌 Cel projektu

- wykrywanie obiektu na podstawie koloru
- śledzenie jego pozycji w czasie (na wideo)
- wizualizacja:
  - konturu obiektu
  - środka (centroidu)
- stworzenie narzędzia do interaktywnego doboru parametrów

---
## 📊 Dane wejściowe
- 🖼️ Obrazy testowe (np. ball.png, kaczka.jpg)
- 🎥 Filmy:
  - moving_ball.mp4
  - moving_ball2.mp4
  - inne testowe nagrania

---

## ⚙️ Pipeline przetwarzania
1️⃣ Konwersja do przestrzeni HSV

    cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

📌 Dlaczego HSV?
- łatwiejsze filtrowanie kolorów niż w RGB
- separacja koloru (Hue) od jasności (Value)

2️⃣ Segmentacja koloru (maska)
- zakresy:
  - Hue
  - Saturation
  - Value
- Obsługa:
  - standardowego zakresu
  - „zawijania” hue (np. czerwony kolor)

🎛️ Interaktywne strojenie (GUI)

Użyto **_ipywidgets_**:

- suwaki:
  - HSV (low / high)
  - filtr medianowy
  - operacje morfologiczne
- 📌 Dzięki temu:
  - można dynamicznie dobrać parametry
  - szybciej osiągnąć stabilne wykrywanie

3️⃣ Redukcja szumu
- Median Blur
- Morphological Closing
- 📌 Efekt:
  - usunięcie drobnych zakłóceń
  - wygładzenie maski

4️⃣ Detekcja obiektu
-  cv2.findContours()
-  wybór największego konturu 
- 📌 Założenie:
  - śledzony obiekt jest największym elementem maski

5️⃣ Wyznaczenie środka (centroid)
- Obliczenia na podstawie momentów:
    
    
    cx = M["m10"] / M["m00"]
    cy = M["m01"] / M["m00"]

6️⃣ Wizualizacja

Na obrazie rysowane są:
- kontur obiektu 🟡
- marker środka ➕
- etykieta (np. "ball")

---
## 🎥 Przetwarzanie wideo

Pipeline dla każdej klatki:

1. konwersja do HSV
2. maska koloru
3. filtracja
4. detekcja konturu
5. rysowanie markerów
6. zapis do pliku wynikowego

📁 Output:
- zapisany plik .mp4 z zaznaczonym obiektem

---

## 🧾 Struktura kodu
- update_mask – generowanie maski HSV
- drawMarker – rysowanie konturu i środka
- update_frame – przetwarzanie pojedynczej klatki
- video – przetwarzanie całego filmu