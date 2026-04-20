# [cite_start]Dokumentacja Testów Akceptacyjnych [cite: 1120]

[cite_start]**Projekt:** System testowania OOB modułu z PyPI [cite: 1121]
[cite_start]**Moduł PyPi:** seaborn [cite: 1123]
[cite_start]**Zespół:** Franciszek Żurawicz, Maciej Radlak, Hubert Miłuch [cite: 1124]
[cite_start]**Data:** 2026-04-20 [cite: 1125]

---

## [cite_start]1. Scenariusze testowe [cite: 1126]

| ID | Nazwa scenariusza | [cite_start]Opis [cite: 1127] |
|---|---|---|
| **TS_01** | Generowanie podstawowego wykresu | Weryfikacja zdolności systemu do tworzenia czytelnych wykresów punktowych dla podanych danych numerycznych. |
| **TS_02** | Grupowanie danych kolorem | Sprawdzenie działania parametru parametryzacji wizualnej (hue) przy kategoryzacji danych. |
| **TS_03** | Obsługa błędnych danych wejściowych | Analiza komunikatów błędów i odporności systemu na pomyłki użytkownika (nieistniejące kolumny). |
| **TS_04** | Skrajnie małe zbiory danych (Edge Case) | Weryfikacja logiki formatowania osi w przypadku otrzymania wyłącznie jednego rekordu. |
| **TS_05** | Tolerancja na braki danych (Edge Case) | Sprawdzenie, czy system potrafi ignorować wartości puste (NaN) bez przerywania działania. |

---

## [cite_start]2. Przypadki testowe [cite: 1134]

### [cite_start]TC_01 - Poprawne wygenerowanie Scatter Plot [cite: 1135]
[cite_start]**Powiązany scenariusz:** TS_01 [cite: 1136]
[cite_start]**Opis:** Użytkownik chce wygenerować wykres punktowy, aby sprawdzić relację między dwiema zmiennymi numerycznymi. [cite: 1137]
[cite_start]**Kroki:** [cite: 1138]
1. Wczytaj poprawny zbiór danych tabelarycznych (np. zbiór `tips`).
2. Wywołaj polecenie `sns.scatterplot()`.
3. Wskaż kolumnę "total_bill" jako oś X.
4. Wskaż kolumnę "tip" jako oś Y.
[cite_start]**Dane wejściowe:** DataFrame z prawidłowymi kolumnami numerycznymi. [cite: 1142]
**Oczekiwany rezultat:** System bezbłędnie zwraca obiekt `Axes`. [cite_start]Na wykresie naniesione są punkty odzwierciedlające wartości z tabeli, a osie są podpisane nazwami kolumn. [cite: 1143]
[cite_start]**Wynik testu:** [ ] PASS   [ ] FAIL [cite: 1144, 1145, 1146]
[cite_start]**Uwagi:** Test zautomatyzowany w ramach `test_scatterplot_happy_path`. [cite: 1148]

---

### [cite_start]TC_02 - Poprawne zastosowanie parametru `hue` [cite: 1149]
[cite_start]**Powiązany scenariusz:** TS_02 [cite: 1150]
[cite_start]**Opis:** Użytkownik chce odróżnić na wykresie kategorie danych przypisując im automatycznie generowane kolory. [cite: 1151]
[cite_start]**Kroki:** [cite: 1152]
1. Wczytaj zbiór danych zawierający zmienną numeryczną i kategoryczną.
2. Wywołaj polecenie `sns.scatterplot()`.
3. Przypisz zmienną kategoryczną do argumentu `hue`.
[cite_start]**Dane wejściowe:** DataFrame z kolumnami numerycznymi i kolumną tekstową z kategoriami. [cite: 1156]
**Oczekiwany rezultat:** Punkty na wykresie pokolorowane są zgodnie z przypisanymi kategoriami. [cite_start]System automatycznie wygenerował i umieścił legendę. [cite: 1157]
[cite_start]**Wynik testu:** [ ] PASS   [ ] FAIL [cite: 1158, 1159, 1160]
[cite_start]**Uwagi:** Zautomatyzowany w `test_scatterplot_hue_parameter`. [cite: 1161]

---

### [cite_start]TC_03 - Reakcja na nieprawidłową nazwę kolumny [cite: 1163]
[cite_start]**Powiązany scenariusz:** TS_03 [cite: 1164]
[cite_start]**Opis:** Weryfikacja czytelności komunikatu błędu w przypadku wystąpienia literówki w nazwie osi. [cite: 1165]
[cite_start]**Kroki:** [cite: 1166]
1. Wczytaj poprawny zbiór danych z kolumną np. "total_bill".
2. Wywołaj polecenie `sns.scatterplot()`.
3. Przekaż do osi Y nazwę kolumny, która nie istnieje w tabeli (np. "literowka_w_nazwie").
[cite_start]**Dane wejściowe:** Oś X = 'poprawna_nazwa', Oś Y = 'literowka_w_nazwie'. [cite: 1170]
**Oczekiwany rezultat:** Wykres nie powstaje. [cite_start]System przerywa działanie i rzuca wyrazisty wyjątek (ValueError / KeyError), jednoznacznie wskazując brakującą kolumnę. [cite: 1171]
[cite_start]**Wynik testu:** [ ] PASS   [ ] FAIL [cite: 1172, 1173, 1174]
**Uwagi:** Brak krytycznej awarii, zachowanie bezpieczne. [cite_start]Zautomatyzowany. [cite: 1175]

---

### [cite_start]TC_04 - Rysowanie wykresu dla jednego rekordu [cite: 1135]
[cite_start]**Powiązany scenariusz:** TS_04 [cite: 1136]
[cite_start]**Opis:** Sprawdzenie logiki dopasowania skali osi przy absolutnym minimum danych wejściowych. [cite: 1137]
[cite_start]**Kroki:** [cite: 1138]
1. Utwórz zbiór danych składający się z tylko jednego wiersza wartości.
2. Wywołaj `sns.scatterplot()` wskazując odpowiednie kolumny.
[cite_start]**Dane wejściowe:** DataFrame: `{'x': [5], 'y': [5]}`. [cite: 1142]
**Oczekiwany rezultat:** Wykres generuje się poprawnie bez błędu matematycznego dzielenia przez zero. [cite_start]Punkt jest widoczny, a osie są automatycznie poszerzone, aby wyśrodkować wartość (np. zakres od 4 do 6). [cite: 1143]
[cite_start]**Wynik testu:** [ ] PASS   [ ] FAIL [cite: 1144, 1145, 1146]
[cite_start]**Uwagi:** [cite: 1148]

---

### [cite_start]TC_05 - Ignorowanie braków w danych (NaN) [cite: 1149]
[cite_start]**Powiązany scenariusz:** TS_05 [cite: 1150]
[cite_start]**Opis:** Weryfikacja zdolności systemu do cichego ignorowania braków pomiarowych bez wywoływania awarii całego skryptu. [cite: 1151]
[cite_start]**Kroki:** [cite: 1152]
1. Wczytaj zbiór danych, w którym występują puste wartości.
2. Wywołaj polecenie wygenerowania histogramu `sns.histplot()` dla "brudnej" kolumny.
[cite_start]**Dane wejściowe:** Lista danych zawierająca obiekty `np.nan` lub `float('nan')`. [cite: 1156]
**Oczekiwany rezultat:** Wykres zostaje narysowany wyłącznie dla poprawnych danych liczbowych. [cite_start]Puste wartości zostają bezpiecznie zignorowane z poziomu obliczeń. [cite: 1157]
[cite_start]**Wynik testu:** [ ] PASS   [ ] FAIL [cite: 1158, 1159, 1160]
[cite_start]**Uwagi:** [cite: 1161]

---

## [cite_start]3. Pokrycie scenariuszy [cite: 1177]

| Scenariusz | Liczba przypadków | [cite_start]Pokrycie | [cite: 1178]
|---|---|---|
| TS_01 | 1 | [cite_start]100% | [cite: 1179]
| TS_02 | 1 | [cite_start]100% | [cite: 1180]
| TS_03 | 1 | [cite_start]100% | [cite: 1181]
| TS_04 | 1 | 100% |
| TS_05 | 1 | 100% |

---

## [cite_start]4. Potencjał automatyzacji [cite: 1182]

Wszystkie scenariusze testów akceptacyjnych w naszym projekcie zostały zweryfikowane pod kątem automatyzacji. [cite_start]Z racji charakteru biblioteki Pythonowej (brak skomplikowanego interfejsu graficznego GUI do przeklikiwania), 100% przypadków nadaje się do włączenia w pipeline CI/CD[cite: 1183, 1184].

| TC_ID | Czy można zautomatyzować? | [cite_start]Uwagi [cite: 1183] |
|---|---|---|
| TC_01 | **TAK** | [cite_start]Zaimplementowano w `test_scatterplot.py` [cite: 1184] |
| TC_02 | **TAK** | [cite_start]Zaimplementowano w `test_scatterplot.py` [cite: 1185] |
| TC_03 | **TAK** | Zaimplementowano z wykorzystaniem wbudowanego `pytest.raises` |
| TC_04 | **TAK** | Wdrożono jako Edge Case w testach jednostkowych |
| TC_05 | **TAK** | Zaimplementowano poprzez wstrzyknięcie wartości biblioteki `numpy` |

---

## [cite_start]5. Wnioski [cite: 1186]

[cite_start]**Co działa poprawnie:** Główny silnik biblioteki Seaborn doskonale i stabilnie radzi sobie z tworzeniem instancji wykresów, nawet jeśli zbiór danych jest mocno obciążony lub zawiera braki (NaN). [cite: 1187]

**Co wymaga poprawy:** Biblioteka czasem zwraca błędy typu KeyError bez dłuższego kontekstu - wymaga to od użytkownika samodzielnego rozszyfrowania nazwy w logach. [cite_start]Dodatkowo rendering legendy dla bardzo dużej ilości unikalnych klas mocno obciąża czas wykonania operacji. [cite: 1188]

**Co było trudne do przetestowania:** Konieczność programowego weryfikowania "aspektów wizualnych". [cite_start]Musieliśmy odpytywać obiekty osi Matplotlib o ich właściwości (np. `len(ax.lines)`), aby sprawdzić, czy Seaborn realnie coś narysował na pustym płótnie. [cite: 1189]
