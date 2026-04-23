# Dokumentacja Testów Akceptacyjnych

**Projekt:** System testowania OOB modułu z PyPI
**Moduł PyPi:** seaborn
**Zespół:** Franciszek Żurawicz, Maciej Radlak, Hubert Miłuch
**Data:** 2026-04-20

---

## 1. Scenariusze testowe

| ID | Nazwa scenariusza | Opis |
|---|---|---|
| **TS_01** | Generowanie podstawowego wykresu | Weryfikacja zdolności systemu do tworzenia czytelnych wykresów punktowych dla podanych danych numerycznych. |
| **TS_02** | Grupowanie danych kolorem | Sprawdzenie działania parametru parametryzacji wizualnej (hue) przy kategoryzacji danych. |
| **TS_03** | Obsługa błędnych danych wejściowych | Analiza komunikatów błędów i odporności systemu na pomyłki użytkownika (nieistniejące kolumny). |
| **TS_04** | Skrajnie małe zbiory danych (Edge Case) | Weryfikacja logiki formatowania osi w przypadku otrzymania wyłącznie jednego rekordu. |
| **TS_05** | Tolerancja na braki danych (Edge Case) | Sprawdzenie, czy system potrafi ignorować wartości puste (NaN) bez przerywania działania. |

---

## 2. Przypadki testowe

### TC_01 - Poprawne wygenerowanie Scatter Plot
**Powiązany scenariusz:** TS_01
**Opis:** Użytkownik chce wygenerować wykres punktowy, aby sprawdzić relację między dwiema zmiennymi numerycznymi.
**Kroki:**
1. Wczytaj poprawny zbiór danych tabelarycznych (np. zbiór `tips`).
2. Wywołaj polecenie `sns.scatterplot()`.
3. Wskaż kolumnę "total_bill" jako oś X.
4. Wskaż kolumnę "tip" jako oś Y.
**Dane wejściowe:** DataFrame z prawidłowymi kolumnami numerycznymi.
**Oczekiwany rezultat:** System bezbłędnie zwraca obiekt `Axes`. Na wykresie naniesione są punkty odzwierciedlające wartości z tabeli, a osie są podpisane nazwami kolumn.
**Wynik testu:** [ ] PASS   [ ] FAIL
**Uwagi:** Test zautomatyzowany w ramach `test_scatterplot_happy_path`.

---

### TC_02 - Poprawne zastosowanie parametru `hue`
**Powiązany scenariusz:** TS_02
**Opis:** Użytkownik chce odróżnić na wykresie kategorie danych przypisując im automatycznie generowane kolory.
**Kroki:**
1. Wczytaj zbiór danych zawierający zmienną numeryczną i kategoryczną.
2. Wywołaj polecenie `sns.scatterplot()`.
3. Przypisz zmienną kategoryczną do argumentu `hue`.
**Dane wejściowe:** DataFrame z kolumnami numerycznymi i kolumną tekstową z kategoriami.
**Oczekiwany rezultat:** Punkty na wykresie pokolorowane są zgodnie z przypisanymi kategoriami. System automatycznie wygenerował i umieścił legendę.
**Wynik testu:** [ ] PASS   [ ] FAIL
**Uwagi:** Zautomatyzowany w `test_scatterplot_hue_parameter`.

---

### TC_03 - Reakcja na nieprawidłową nazwę kolumny
**Powiązany scenariusz:** TS_03
**Opis:** Weryfikacja czytelności komunikatu błędu w przypadku wystąpienia literówki w nazwie osi.
**Kroki:**
1. Wczytaj poprawny zbiór danych z kolumną np. "total_bill".
2. Wywołaj polecenie `sns.scatterplot()`.
3. Przekaż do osi Y nazwę kolumny, która nie istnieje w tabeli (np. "literowka_w_nazwie").
**Dane wejściowe:** Oś X = 'poprawna_nazwa', Oś Y = 'literowka_w_nazwie'.
**Oczekiwany rezultat:** Wykres nie powstaje. System przerywa działanie i rzuca wyrazisty wyjątek (ValueError / KeyError), jednoznacznie wskazując brakującą kolumnę.
**Wynik testu:** [ ] PASS   [ ] FAIL
**Uwagi:** Brak krytycznej awarii, zachowanie bezpieczne. Zautomatyzowany.

---

### TC_04 - Rysowanie wykresu dla jednego rekordu
**Powiązany scenariusz:** TS_04
**Opis:** Sprawdzenie logiki dopasowania skali osi przy absolutnym minimum danych wejściowych.
**Kroki:**
1. Utwórz zbiór danych składający się z tylko jednego wiersza wartości.
2. Wywołaj `sns.scatterplot()` wskazując odpowiednie kolumny.
**Dane wejściowe:** DataFrame: `{'x': [5], 'y': [5]}`.
**Oczekiwany rezultat:** Wykres generuje się poprawnie bez błędu matematycznego dzielenia przez zero. Punkt jest widoczny, a osie są automatycznie poszerzone, aby wyśrodkować wartość (np. zakres od 4 do 6).
**Wynik testu:** [ ] PASS   [ ] FAIL
**Uwagi:** Zautomatyzowany w testach jednostkowych jako Edge Case.

---

### TC_05 - Ignorowanie braków w danych (NaN)
**Powiązany scenariusz:** TS_05
**Opis:** Weryfikacja zdolności systemu do cichego ignorowania braków pomiarowych bez wywoływania awarii całego skryptu.
**Kroki:**
1. Wczytaj zbiór danych, w którym występują puste wartości.
2. Wywołaj polecenie wygenerowania histogramu `sns.histplot()` dla "brudnej" kolumny.
**Dane wejściowe:** Lista danych zawierająca obiekty `np.nan` lub `float('nan')`.
**Oczekiwany rezultat:** Wykres zostaje narysowany wyłącznie dla poprawnych danych liczbowych. Puste wartości zostają bezpiecznie zignorowane z poziomu obliczeń.
**Wynik testu:** [ ] PASS   [ ] FAIL
**Uwagi:** Zautomatyzowany poprzez wstrzyknięcie wartości biblioteki `numpy`.

---

## 3. Pokrycie scenariuszy

| Scenariusz | Liczba przypadków | Pokrycie |
|---|---|---|
| TS_01 | 1 | 100% |
| TS_02 | 1 | 100% |
| TS_03 | 1 | 100% |
| TS_04 | 1 | 100% |
| TS_05 | 1 | 100% |

---

## 4. Potencjał automatyzacji

Wszystkie scenariusze testów akceptacyjnych w naszym projekcie zostały zweryfikowane pod kątem automatyzacji. Z racji charakteru biblioteki Pythonowej (brak skomplikowanego interfejsu graficznego GUI do przeklikiwania), 100% przypadków nadaje się do włączenia w pipeline CI/CD.

| TC_ID | Czy można zautomatyzować? | Uwagi |
|---|---|---|
| TC_01 | **TAK** | Zaimplementowano w `test_scatterplot.py` |
| TC_02 | **TAK** | Zaimplementowano w `test_scatterplot.py` |
| TC_03 | **TAK** | Zaimplementowano z wykorzystaniem wbudowanego `pytest.raises` |
| TC_04 | **TAK** | Wdrożono jako Edge Case w testach jednostkowych |
| TC_05 | **TAK** | Zaimplementowano poprzez wstrzyknięcie wartości biblioteki `numpy` |

---

## 5. Wnioski

**Co działa poprawnie:** Główny silnik biblioteki Seaborn doskonale i stabilnie radzi sobie z tworzeniem instancji wykresów, nawet jeśli zbiór danych jest mocno obciążony lub zawiera braki (NaN).

**Co wymaga poprawy:** Biblioteka czasem zwraca błędy typu KeyError bez dłuższego kontekstu - wymaga to od użytkownika samodzielnego rozszyfrowania nazwy w logach. Dodatkowo rendering legendy dla bardzo dużej ilości unikalnych klas mocno obciąża czas wykonania operacji.

**Co było trudne do przetestowania:** Konieczność programowego weryfikowania "aspektów wizualnych". Musieliśmy odpytywać obiekty osi Matplotlib o ich właściwości (np. `len(ax.lines)`), aby sprawdzić, czy Seaborn realnie coś narysował na pustym płótnie.
