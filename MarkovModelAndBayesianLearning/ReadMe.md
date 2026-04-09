# Papier–Kamień–Nożyce
Bayesian Learning & Hidden Markov Model

Projekt przedstawia symulację gry Papier–Kamień–Nożyce, 
w której jeden gracz stosuje strategię probabilistyczną, 
a drugi uczy się jej w czasie, 
wykorzystując twierdzenie Bayesa oraz koncepcję łańcuchów Markowa.

--- 

## Opis projektu

W symulacji bierze udział dwóch graczy:

### 🎲 Gracz 1 — strategia probabilistyczna
- Korzysta z ustalonej macierzy przejść (Hidden Markov Model)
- Kolejny ruch zależy od poprzedniego ruchu
- Zachowanie jest losowe, ale kontrolowane przez rozkład prawdopodobieństwa

### 🎲 Gracz 2 — uczący się przeciwnik
- Obserwuje ruchy Gracza 1
- Aktualizuje swoje przekonania za pomocą aktualizacji bayesowskiej
- Szacuje macierz przejść przeciwnika
- Wybiera kontr-ruch, aby maksymalizować szansę wygranej

---

## Wykorzystane koncepcje
- Łańcuchy Markowa (Markov Chains)
-  Ukryty Model Markowa (Hidden Markov Model)
-  Prawdopodobieństwo warunkowe
-  Twierdzenie Bayesa
-  Uczenie przez obserwację (frequency-based estimation)


--- 

## Działanie:

1. Gracz 1 generuje ruch na podstawie:
    - rozkładu początkowego
    - macierzy przejść

2. Gracz 2:
   - zlicza przejścia między ruchami
   - normalizuje dane (estymacja prawdopodobieństw)
   - przewiduje następny ruch przeciwnika
   - wybiera ruch, który go pokona
   - stosuje uproszczoną wersję twierdzenia Bayesa:


    P(A|B) = (P(B|A) * P(A)) / P(B)

### ▶️ Symulacja
- 🔢 Liczba rund: 1000 
- 📊 Śledzenie wyników:
    - liczba wygranych obu graczy
    - remisy 
- 📉 Generowany wykres:
    - skumulowane wygrane
    - przewaga jednego z graczy

### 📈 Przykładowy wynik
Gracz 2 stopniowo uczy się strategii przeciwnika
Po pewnym czasie zaczyna wygrywać częściej

Wyuczona macierz przejść zbliża się do rzeczywistej

### 🧾 Wyjście programu

Po zakończeniu symulacji program wypisuje:

- 🏆 Zwycięzcę
- 📊 Statystyki:
  - wygrane Gracza 1
  - wygrane Gracza 2
  - remisy
- 📉 Wykres wyników
- 🔢 Macierze przejść:
  - rzeczywista (Gracz 1)
  - wyuczona (Gracz 2)

--- 

## 🧩 Struktura kodu
- *sampleFromDict* – losowanie na podstawie rozkładu
- *ruch1Gracz* – generowanie ruchu Gracza 1
- *updateCounts* – aktualizacja obserwacji
- *BayesTheorem* – obliczenia probabilistyczne
- *ruch2gracza* – decyzja Gracza 2
- symulacja + wizualizacja (*matplotlib*)