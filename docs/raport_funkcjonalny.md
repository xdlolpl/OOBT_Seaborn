
# Raport z Testów Funkcjonalnych

**Osoba odpowiedzialna:** Franciszek Żurawicz
**Cel:** Sprawdzenie poprawności działania wybranych funkcji biblioteki z perspektywy typowego użytkownika.

## 1. Architektura Testów
Wszystkie testy korzystają z backendu Matplotlib `Agg` (`matplotlib.use('Agg')`), co rozwiązuje częsty problem z biblioteką `tkinter` podczas uruchamiania testów wizualnych w zautomatyzowanych pipeline'ach (CI/CD) bez interfejsu graficznego. Każdy test kończy się wywołaniem `plt.close()`, co gwarantuje czyszczenie pamięci i izolację testów. Do weryfikacji używamy właściwości obiektu `Axes` (np. `ax.collections`, `ax.get_xlabel()`).

## 2. Happy Path (Szczęśliwe Ścieżki)
Testy weryfikujące główne funkcjonalności z poprawnymi danymi wejściowymi.

* **TC_01: Rysowanie podstawowego wykresu (Scatter Plot)**
    * **Implementacja:** `test_scatterplot_happy_path` (`tests/test_scatterplot.py`)
    * **Weryfikacja:** System poprawnie zwraca obiekt `Axes`, nakłada punkty (`len(ax.collections) > 0`) i nadaje osiom odpowiednie nazwy bazując na kluczach słownika/tabeli.
* **TC_02: Dynamiczna zmiana palet kolorów**
    * **Implementacja:** `test_scatterplot_multiple_palettes` (`tests/test_advanced_features.py`)
    * **Weryfikacja:** Z użyciem dekoratora `@pytest.mark.parametrize` upewniono się, że biblioteka poprawnie przyjmuje popularne palety predefiniowane (m.in. `deep`, `colorblind`).
* **TC_03: Kategoryzacja danych (parametr `hue`)**
    * **Implementacja:** `test_scatterplot_hue_parameter` (`tests/test_scatterplot.py`)
    * **Weryfikacja:** Sprawdzono, czy po przekazaniu kolumny kategorycznej Seaborn nie tylko koloruje punkty, ale też automatycznie generuje poprawnie zatytułowaną legendę.

## 3. Negative Path (Ścieżki Negatywne)
Weryfikacja obsługi błędów użytkownika (oczekujemy czytelnych komunikatów).

* **TC_04: Obsługa nieistniejących kolumn**
    * **Implementacja:** `test_scatterplot_invalid_column` (`tests/test_scatterplot.py`)
    * **Weryfikacja:** Przy podaniu literówki w parametrze `y`, test poprawnie używa kontekstu `with pytest.raises(ValueError):`, udowadniając, że Seaborn zgłasza błąd i przerywa działanie zamiast cicho ignorować problem.

## 4. Edge Cases (Przypadki brzegowe)
Sytuacje skrajne weryfikujące logikę Matplotliba pod maską Seaborna.

* **TC_05: Renderowanie pustych ramek danych**
    * **Implementacja:** `test_boxplot_empty_dataframe`
    * **Weryfikacja:** System jest odporny na brak wierszy. Rysuje układ współrzędnych bez rzucania wyjątków (`len(ax.lines) == 0`).
* **TC_06: Tolerancja na braki w danych (NaN)**
    * **Implementacja:** `test_histplot_with_nans`
    * **Weryfikacja:** Zgodnie z założeniami z dokumentacji, Seaborn cicho ignoruje braki typu `float('nan')` i poprawnie rysuje słupki (patches) dla pozostałych wartości liczbowych.
* **TC_07: Renderowanie kategoryczne na wykresach osi liczbowych (Lineplot)**
    * **Implementacja:** `test_lineplot_categorical_data`
    * **Weryfikacja:** Zamiast zgłaszać `TypeError` przy wykresie liniowym opartym na tekście, biblioteka poprawnie mapuje ciągi znaków jako odrębne kategorie.
* **TC_08: Skrajne dostosowanie granic osi (Limits)**
    * **Implementacja:** `test_scatterplot_data_bounds` (`tests/test_visual_integrity.py`)
    * **Weryfikacja:** Test systemowy pobierający realny dataset ("tips"). Udowadnia, że Seaborn automatycznie rozszerza płótno (`ax.get_xlim()[1]`) tak, aby nie ucinać skrajnych wartości punktów.
