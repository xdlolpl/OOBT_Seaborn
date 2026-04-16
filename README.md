# Projekt testowania biblioteki Seaborn

## Cel projektu
Celem projektu jest stworzenie prostego systemu testowania typu "out-of-the-box" dla biblioteki **Seaborn** (Python), dostępnej w repozytorium PyPI.

## Strategia testowa
Projekt skupi się na testowaniu najnowszej stabilnej wersji biblioteki Seaborn. Testy mają weryfikować kluczowe funkcjonalności biblioteki z perspektywy typowego użytkownika, który tworzy wizualizacje danych.

*   **Testy funkcjonalne:** Sprawdzą poprawność działania wybranych funkcji biblioteki, takich jak tworzenie różnych typów wykresów (np. `scatterplot`, `histplot`) i ich podstawowe parametryzowanie. Oczekiwane rezultaty to utworzenie obiektu wykresu lub pliku graficznego bez błędów.
*   **Testy wydajnościowe:** Zmierzą czas generowania wykresów dla zbiorów danych o różnej wielkości. Pozwoli to na wstępną ocenę, jak biblioteka radzi sobie z większymi danymi.
*   **Scenariusze testów akceptacyjnych:** Zdefiniują sytuacje z życia wzięte, w których biblioteka jest używana, wraz z kryteriami sukcesu (np. "użytkownik jest w stanie wygenerować wykres korelacji dla podanego zbioru danych").

Pipeline CI/CD (GitHub Actions) zostanie skonfigurowany do automatycznej instalacji Seaborna i uruchamiania wszystkich przygotowanych testów.

## Scenariusze

## 1. Happy Path (Szczęśliwa ścieżka)

*Celem tej kategorii jest weryfikacja, czy główne, podstawowe funkcje biblioteki działają poprawnie przy użyciu prawidłowych i oczekiwanych danych wejściowych.*

### Scenariusz: Rysowanie podstawowego wykresu punktowego (Scatter Plot)
- **Cel testu:** Upewnienie się, że wywołanie funkcji `sns.scatterplot()` z poprawną ramką danych (DataFrame) oraz prawidłowymi nazwami kolumn dla osi X i Y, faktycznie zwraca obiekt wykresu Matplotlib i nie zgłasza żadnych błędów.
- **Warunki początkowe:** Dostępna jest ramka danych `pandas.DataFrame` z kolumnami numerycznymi, np. `'total_bill'` i `'tip'` (z popularnego zbioru `tips`).
- **Kroki:**
    1. Zaimportować biblioteki `seaborn` i `matplotlib.pyplot`.
    2. Wywołać funkcję `sns.scatterplot(data=df, x='total_bill', y='tip')`.
- **Oczekiwany rezultat:** Funkcja zwraca obiekt `Axes` z biblioteki Matplotlib. Wykres zostaje utworzony bez zgłaszania wyjątków.

### Scenariusz: Kolorowanie danych według kategorii (parametr `hue`)
- **Cel testu:** Weryfikacja, czy dodanie argumentu `hue="kategoria"` poprawnie przypisuje różne kolory punktom na wykresie na podstawie tej kolumny.
- **Warunki początkowe:** Dostępna jest ramka danych z kolumną numeryczną (`x`) i kolumną kategoryczną (`category`).
- **Kroki:**
    1. Wywołać funkcję `sns.scatterplot(data=df, x='x', y='x', hue='category')`.
    2. Pobrać listę obiektów reprezentujących punkty (kolekcje) z osi wykresu.
- **Oczekiwany rezultat:** Liczba unikalnych kolorów na wykresie jest równa liczbie unikalnych kategorii w kolumnie `category`. Zwrócony obiekt `Axes` zawiera legendę z nazwami kategorii.

### Scenariusz: Zmiana globalnego stylu wykresów
- **Cel testu:** Sprawdzenie, czy użycie funkcji `sns.set_theme(style="darkgrid")` faktycznie zmienia tło kolejnych generowanych wykresów na ciemną siatkę.
- **Warunki początkowe:** Domyślny styl Seaborna jest aktywny.
- **Kroki:**
    1. Wywołać `sns.set_theme(style="darkgrid")`.
    2. Wygenerować prosty wykres (np. `sns.histplot(data=[1,2,3,4,5])`).
- **Oczekiwany rezultat:** Wygenerowany wykres posiada ciemne tło z białą siatką. Różni się to wizualnie (można to sprawdzić przez porównanie koloru tła figury) od wykresu wygenerowanego przed zmianą stylu.

---

## 2. Negative Path (Ścieżki negatywne)

*Ta kategoria testuje, jak biblioteka radzi sobie z błędami po stronie użytkownika. Oczekujemy czytelnych komunikatów błędów, a nie cichego ignorowania problemu lub awarii.*

### Scenariusz: Podanie nieistniejących nazw kolumn
- **Cel testu:** Sprawdzenie, co się stanie, gdy użytkownik wpisze nieprawidłową nazwę kolumny dla parametru `x` lub `y`.
- **Warunki początkowe:** Dostępna jest ramka danych z kolumną `'poprawna_nazwa'`.
- **Kroki:**
    1. Wywołać `sns.scatterplot(data=df, x='poprawna_nazwa', y='literowka_w_nazwie')`.
- **Oczekiwany rezultat:** Wywołanie funkcji zgłasza wyjątek typu `KeyError`. Komunikat błędu jasno wskazuje, która nazwa kolumny (`'literowka_w_nazwie'`) nie została znaleziona w ramce danych.

### Scenariusz: Niezgodność typów danych
- **Cel testu:** Próba wykonania operacji wymagającej danych liczbowych na danych tekstowych i weryfikacja, czy błąd jest komunikowany w zrozumiały sposób.
- **Warunki początkowe:** Ramka danych zawiera kolumnę z danymi tekstowymi, np. `['imie1', 'imie2', 'imie3']`.
- **Kroki:**
    1. Wywołać `sns.lineplot(data=df, x=df.index, y='kolumna_tekstowa')`.
- **Oczekiwany rezultat:** Funkcja zgłasza wyjątek, najprawdopodobniej `TypeError` lub `ValueError`, z komunikatem informującym, że nie można przekonwertować danych tekstowych na liczby zmiennoprzecinkowe wymagane do narysowania linii.

---

## 3. Edge Cases (Przypadki brzegowe)

*Tutaj sprawdzamy zachowanie biblioteki w sytuacjach nietypowych, które mogą wystąpić na granicy jej możliwości lub przy specyficznych danych. Celem jest sprawdzenie stabilności i przewidywalności.*

### Scenariusz: Przekazanie całkowicie pustej ramki danych
- **Cel testu:** Weryfikacja zachowania funkcji `sns.boxplot()`, gdy zbiór danych nie zawiera żadnych wierszy, ale ma zdefiniowane kolumny.
- **Warunki początkowe:** Pusta ramka danych (`df = pd.DataFrame(columns=['A', 'B'])`).
- **Kroki:**
    1. Wywołać `sns.boxplot(data=df)`.
- **Oczekiwany rezultat:** Funkcja nie zgłasza błędu. Zamiast tego zwraca obiekt `Axes` z prawidłowo zdefiniowanymi etykietami osi (kolumna 'A', 'B'), ale bez żadnych zaznaczonych danych (pudła nie są narysowane). Jest to zachowanie bezpieczne i informacyjne.

### Scenariusz: Dane z ogromną ilością braków (NaN)
- **Cel testu:** Upewnienie się, że Seaborn radzi sobie z danymi zawierającymi wartości puste (NaN) i nie przerywa działania.
- **Warunki początkowe:** Ramka danych, w której 50% wartości w kluczowej kolumnie to `np.nan`.
- **Kroki:**
    1. Wywołać `sns.histplot(data=df, x='kolumna_z_nanami')`.
- **Oczekiwany rezultat:** Histogram zostaje poprawnie wygenerowany. Liczba obserwacji (wysokość słupków) odpowiada liczbie niepustych wartości w kolumnie. Seaborn domyślnie ignoruje wartości `NaN`, co jest zgodne z oczekiwaniami.

### Scenariusz: Wykres dla tylko jednego rekordu danych
- **Cel testu:** Sprawdzenie, czy osie X i Y odpowiednio dobierają skalę, gdy otrzymają tylko jedną unikalną wartość.
- **Warunki początkowe:** Ramka danych zawiera dokładnie jeden wiersz z wartościami, np. `{'x': 5, 'y': 5}`.
- **Kroki:**
    1. Wywołać `sns.scatterplot(data=df, x='x', y='y')`.
- **Oczekiwany rezultat:** Na wykresie pojawia się pojedynczy punkt w okolicach środka. Zakres osi nie jest ustawiony dokładnie na wartość 5 (np. od 5 do 5), ale jest nieco rozszerzony (np. od 4 do 6), co pozwala na wizualną lokalizację punktu. Biblioteka radzi sobie z tym przypadkiem bez błędu.

### Scenariusz: Ekstremalnie duży zbiór danych
- **Cel testu:** Próba wygenerowania wykresu dla bardzo dużej liczby punktów (np. miliona wierszy) w celu sprawdzenia, czy biblioteka nie ulegnie awarii, a czas wykonania będzie akceptowalny.
- **Warunki początkowe:** Wygenerowana ramka danych z 1,000,000 losowych punktów.
- **Kroki:**
    1. Zmierzyć czas wykonania funkcji `sns.scatterplot(data=large_df, x='col1', y='col2')`.
    2. Sprawdzić, czy proces nie został przerwany błędem (np. `MemoryError`).
- **Oczekiwany rezultat:** Funkcja wykonuje się w rozsądnym czasie (np. poniżej 10-15 sekund) i zwraca obiekt wykresu. Seaborn (poprzez Matplotlib) może dokonać zagregowania (rasteryzacji) punktów, aby nie przeciążać interfejsu graficznego, ale ostatecznie wykres powstaje.



## Podział ról w zespole

*   **Hubert Miłuch:** Administrator repozytorium, konfiguracja pipeline'u GitHub Actions.
*   **`https://github.com/dawadwadwadw`:** Projektowanie i implementacja testów funkcjonalnych.
*   **`https://github.com/MaciejRadlak`:** Projektowanie i implementacja testów wydajnościowych, dokumentacja

## 🛠️ Zadania administratora (DevOps) – Hubert Miłuch

Zgodnie z podziałem ról, Hubert pełni funkcję administratora repozytorium oraz odpowiada za DevOps. Jego zadaniem jest stworzenie i utrzymanie infrastruktury, która automatyzuje testowanie projektu.

---

### 1. 🤖 Pipeline CI/CD (GitHub Actions)

**Opis zadania:**
Utworzenie automatycznego pipeline'u testowego w GitHub Actions.

**Kroki do wykonania:**
- Utworzenie folderu:
  ```
  .github/workflows/
  ```
- Dodanie pliku konfiguracyjnego, np.:
  ```
  testy.yml
  ```
- Skonfigurowanie pipeline’u tak, aby:
  - uruchamiał się przy każdym `push` i `pull request`
  - instalował Python 3.11
  - instalował zależności z `requirements.txt`
  - uruchamiał testy poleceniem:
    ```
    pytest
    ```

**Cel:**
Automatyczne testowanie kodu przy każdej zmianie w repozytorium.

---

### 2. 🔒 Ochrona gałęzi `main` (Branch Protection)

**Opis zadania:**
Zabezpieczenie głównej gałęzi repozytorium przed bezpośrednimi zmianami.

**Kroki do wykonania:**
- Przejście do:
  ```
  Settings → Branches → Add branch protection rule
  ```
- Ustawienie reguł:
  - blokada bezpośredniego `push` do `main`
  - wymaganie Pull Requestów
  - wymaganie przejścia testów CI/CD przed merge

**Cel:**
Zapewnienie, że kod trafiający do `main` jest sprawdzony i zatwierdzony.

---

### 3. 📋 Zarządzanie zadaniami (Issues & Milestones)

**Opis zadania:**
Organizacja pracy zespołu przy użyciu narzędzi GitHuba.

**Kroki do wykonania:**
- Utworzenie kilku **Milestones** (np. etapy projektu)
- Rozbicie projektu na mniejsze zadania (**Issues**)
- Przypisanie zadań do członków zespołu

**Cel:**
Lepsza organizacja pracy i pokazanie podejścia Agile.

---

### 4. 👀 Code Review

**Opis zadania:**
Weryfikacja kodu przesyłanego przez członków zespołu.

**Kroki do wykonania:**
- Przeglądanie Pull Requestów
- Dodawanie komentarzy i sugestii
- Zatwierdzanie zmian (*Approve*)

**Cel:**
Utrzymanie wysokiej jakości kodu i spójności projektu.

---

### 📌 Podsumowanie

Hubert odpowiada za:
- automatyzację testów (CI/CD),
- bezpieczeństwo repozytorium,
- organizację pracy zespołu,
- kontrolę jakości kodu.

---

## 📅 Harmonogram projektu

Projekt realizowany jest w czasie około **2,5 miesiąca**, zgodnie z wymaganiami projektu OOB PyPI.  
Praca została podzielona na etapy odpowiadające punktom kontrolnym.

---

## 🟢 Etap 1 – Organizacja projektu (Punkt kontrolny 1)
📆 **Termin: do 17.04.2026**

**Zakres:**
- Utworzenie repozytorium GitHub
- Przygotowanie README (cel + strategia testowa)
- Określenie ról w zespole
- Ustalenie kanałów komunikacji
- Przygotowanie wstępnych scenariuszy testowych
- Stworzenie harmonogramu projektu

**Odpowiedzialni:**
- Cały zespół
- Hubert (repozytorium)

---

## 🔵 Etap 2 – Zarządzanie kodem (Punkt kontrolny 2)
📆 **Termin: do 30.04.2026**

**Zakres:**
- Praca na branchach
- Tworzenie Issues (podział zadań)
- Praca z Pull Requestami
- Code review
- Konfiguracja Branch Protection
- Wstępna konfiguracja CI/CD (GitHub Actions)

**Odpowiedzialni:**
- Hubert (CI/CD, repo)
- Cały zespół (PR, Issues)

---

## 🟡 Etap 3 – Implementacja testów (Punkt kontrolny 3)
📆 **Termin: do 15.05.2026**

**Zakres:**
- Implementacja testów funkcjonalnych (3–5)
- Implementacja testów wydajnościowych (1–2)
- Dopracowanie scenariuszy testów akceptacyjnych
- Uruchamianie pipeline (manualne)
- Dodanie raportowania wyników testów

**Odpowiedzialni:**
- Ty (testy funkcjonalne)
- Maciej (testy wydajnościowe)
- Hubert (pipeline)

---

## 🔴 Etap 4 – Finalizacja projektu (Release)
📆 **Termin: do 29.05.2026**

**Zakres:**
- Uporządkowanie repozytorium
- Finalna dokumentacja
- Sprawdzenie działania pipeline
- Code review całego projektu
- Przygotowanie prezentacji
- Opis problemów i wniosków

**Odpowiedzialni:**
- Cały zespół

---

## 📊 Podsumowanie etapów

| Etap | Nazwa | Termin |
|------|------|--------|
| 1 | Organizacja projektu | 17.04.2026 |
| 2 | Zarządzanie kodem | 30.04.2026 |
| 3 | Testowanie | 15.05.2026 |
| 4 | Finalizacja | 29.05.2026 |

---

## 🚀 Metodyka pracy

Projekt realizowany zgodnie z podejściem iteracyjnym:

- praca na osobnych branchach
- wykorzystanie Pull Requestów
- code review przed merge
- zarządzanie zadaniami przez GitHub Issues
- automatyczne testy (CI/CD)

---

## 📌 Uwagi

- Pipeline uruchamiana manualnie zgodnie z wymaganiami projektu
- Testy skupiają się na realnych scenariuszach użycia biblioteki Seaborn
- Projekt kładzie nacisk na organizację pracy zespołowej oraz czytelność kodu i dokumentacji


## Kanały komunikacji
*   **GitHub Issues:** Do śledzenia zadań i błędów.
*   **Discord/Messenger:** Do codziennej, bieżącej komunikacji w zespole.
