# Scenariusze Testów Akceptacyjnych - Biblioteka Seaborn

W niniejszym dokumencie zdefiniowano scenariusze akceptacyjne dla systemu wizualizacji danych (moduł `seaborn`). Testy te mają na celu weryfikację, czy system spełnia wymagania użytkownika i czy pozwala mu skutecznie realizować jego zadania biznesowe/analityczne.

---

## 1. Happy Path: Generowanie podstawowego wykresu

**ID:** TA-SEABORN-01
**Cel:** Użytkownik chce szybko wygenerować czytelny wykres punktowy (Scatter Plot) na podstawie posiadanych danych tabelarycznych, aby sprawdzić relację między dwiema zmiennymi.

**Warunki początkowe:** Dostępny jest poprawnie sformatowany zbiór danych tabelarycznych (np. zawierający informacje o rachunkach i napiwkach).

**Kroki:**
1. Wczytaj zbiór danych do programu.
2. Wywołaj polecenie wygenerowania wykresu punktowego.
3. Wskaż kolumnę "kwota rachunku" jako oś X oraz kolumnę "napiwek" jako oś Y.
4. Wyświetl gotowy wykres.

**Oczekiwany rezultat:** System bezbłędnie generuje obiekt graficzny. Na ekranie pojawia się czytelny wykres punktowy, osie są poprawnie opisane nazwami wybranych kolumn, a punkty na wykresie odpowiadają wartościom z tabeli. Użytkownik osiąga swój cel analityczny.

---

## 2. Happy Path: Grupowanie danych kolorem (Parametr `hue`)

**ID:** TA-SEABORN-02
**Cel:** Użytkownik chce wizualnie odróżnić różne kategorie danych na jednym wykresie, aby łatwiej zidentyfikować trendy w poszczególnych grupach (np. czy kobiety dają inne napiwki niż mężczyźni).

**Warunki początkowe:** Dostępny jest zbiór danych zawierający zmienne liczbowe oraz co najmniej jedną zmienną kategoryczną (tekstową/grupującą).

**Kroki:**
1. Wczytaj zbiór danych.
2. Wywołaj polecenie wygenerowania wykresu punktowego dla dwóch zmiennych liczbowych.
3. Użyj argumentu grupowania (hue), przypisując mu kolumnę kategoryczną (np. "płeć").
4. Wyświetl wykres.

**Oczekiwany rezultat:** Powstaje wykres, na którym punkty są automatycznie pokolorowane różnymi barwami w zależności od przynależności do kategorii. System automatycznie generuje i umieszcza na wykresie czytelną legendę tłumaczącą znaczenie kolorów.

---

## 3. Negative Path: Obsługa błędu wprowadzania danych

**ID:** TA-SEABORN-03
**Cel:** Weryfikacja odporności systemu i jakości komunikatów o błędach w przypadku pomyłki użytkownika (wpisanie nieistniejącej nazwy zmiennej).

**Warunki początkowe:** Dostępny jest zbiór danych z kolumnami "total_bill" oraz "tip".

**Kroki:**
1. Wczytaj zbiór danych.
2. Wywołaj polecenie wygenerowania wykresu.
3. Wskaż poprawną nazwę dla osi X ("total_bill").
4. Przypadkowo podaj błędną nazwę dla osi Y, która nie istnieje w tabeli (np. "tipp").

**Oczekiwany rezultat:** Wykres nie zostaje wygenerowany. System nie ulega jednak krytycznej awarii (np. zamknięciu aplikacji). Proces zostaje przerwany, a użytkownik otrzymuje czytelny komunikat błędu (`KeyError`), który jasno informuje go, że kolumna "tipp" nie została znaleziona. 

---

## 4. Edge Case: Logika wizualizacji minimalnych danych

**ID:** TA-SEABORN-04
**Cel:** Sprawdzenie, czy system potrafi inteligentnie sformatować przestrzeń wykresu, gdy użytkownik wizualizuje skrajnie małą ilość danych (np. po restrykcyjnym filtrowaniu).

**Warunki początkowe:** Dostępny jest zbiór danych składający się z dokładnie jednego rekordu.

**Kroki:**
1. Wczytaj jednoelementowy zbiór danych.
2. Wywołaj polecenie wygenerowania wykresu dla tych zmiennych.
3. Wyświetl wykres.

**Oczekiwany rezultat:** System generuje wykres z jednym punktem bez zgłaszania błędów matematycznych (np. dzielenia przez zero). System automatycznie rozszerza zakres na osiach, aby punkt był wycentrowany i wyraźnie widoczny.

---

## 5. Edge Case: Tolerancja na braki w danych (Wartości `NaN`)

**ID:** TA-SEABORN-05
**Cel:** Użytkownik pracuje na "brudnych" danych analitycznych i chce wygenerować wykres, mimo że w tabeli brakuje niektórych pomiarów. System nie powinien karać użytkownika za niekompletne dane.

**Warunki początkowe:** Dostępny jest zbiór danych, w którym znaczna część rekordów w kluczowej kolumnie jest pusta (wartości `NaN` / Null).

**Kroki:**
1. Wczytaj zbiór danych z brakami.
2. Wywołaj polecenie wygenerowania histogramu dla kolumny zawierającej braki.
3. Wyświetl wykres.

**Oczekiwany rezultat:** System nie ulega awarii. Zamiast tego po cichu ignoruje puste wartości i poprawnie rysuje histogram wyłącznie dla istniejących danych liczbowych. Oś Y (liczba wystąpień) odzwierciedla tylko liczbę poprawnych rekordów.