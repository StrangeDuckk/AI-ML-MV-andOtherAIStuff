# 🧠 Retrieval-Augmented Generation (RAG)
LLM, Qwen, Semantic Search, NLP

Projekt przedstawia implementację systemu 
RAG (Retrieval-Augmented Generation), 
który łączy model językowy (LLM) z wyszukiwaniem 
wiedzy w dokumentach, umożliwiając generowanie bardziej 
trafnych i kontekstowych odpowiedzi.

---
## 📌 Cel projektu

- zbudowanie systemu Question Answering opartego o dokumenty
- integracja modelu LLM (Qwen) z mechanizmem wyszukiwania
- poprawa jakości odpowiedzi poprzez kontekst
- demonstracja działania pipeline’u RAG

---

## 🧠 Czym jest RAG?

RAG = **Retrieval + Generation**

1. 🔍 Retrieval – wyszukiwanie najbardziej pasujących fragmentów tekstu
2. ✍️ Generation – generowanie odpowiedzi przez model LLM na podstawie kontekstu

📌 Dzięki temu:
- model nie „zgaduje” odpowiedzi
- korzysta z realnych danych

---

## ⚙️ Pipeline systemu
1️⃣ Przygotowanie danych
- wczytanie dokumentów (tekst / pliki)
- podział na fragmenty (chunking)

2️⃣ Embeddingi
- zamiana tekstu na wektory (embeddingi)
- reprezentacja semantyczna danych
- 📌 Efekt:
  - podobne znaczeniowo teksty → blisko w przestrzeni wektorowej

3️⃣ Wyszukiwanie (Retrieval)
- porównanie zapytania z embeddingami
- wybór najbardziej podobnych fragmentów 
- 📌 Techniki:
  - similarity search (np. cosine similarity)

4️⃣ Generowanie odpowiedzi (LLM – Qwen)
- przekazanie:
  - pytania użytkownika
  - znalezionego kontekstu
- model generuje odpowiedź opartą na danych
  
---

## 💬 Przykładowy przepływ
1. Użytkownik zadaje pytanie 
2. System wyszukuje powiązane fragmenty 
3. LLM generuje odpowiedź bazując na kontekście

---

## 🧾 Struktura projektu
- preprocessing danych
- generowanie embeddingów
- wyszukiwanie kontekstu
- integracja z modelem Qwen
- generowanie odpowiedzi