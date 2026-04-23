
# Raport z Testów Wydajnościowych (Performance Tests)

**Osoba odpowiedzialna:** Maciej Radlak
**Cel:** Zmierzenie czasu generowania wykresów dla zbiorów danych o różnej wielkości i weryfikacja stabilności biblioteki Seaborn pod wysokim obciążeniem.

## Metodologia Pomiarów
Ze względu na specyfikę środowisk wirtualnych i Pythona, pomiary pojedyncze mogą być zaburzone przez:
1.  **Anomalie sprzętowe** (procesy systemowe w tle).
2.  **Zarządzanie pamięcią** (losowe uruchomienia *Garbage Collectora*).
Dlatego każdy test wykorzystuje funkcję `time.perf_counter()` i składa się z fazy "rozgrzewki" silnika renderującego, po której następuje **5 niezależnych iteracji**. Ostatecznym wynikiem weryfikowanym w asercji jest średnia (odrzucająca skrajne piki systemowe), co gwarantuje stabilność testu. Wszystkie testy uruchamiano z użyciem bezokienkowego backendu `Agg`.

---

## Scenariusz 1: Ekstremalnie duży zbiór danych (Wolumen)
**Plik testowy:** `tests/test_performance.py`

**Opis testu:** Weryfikacja odporności biblioteki na ogromną ilość punktów (1 500 000 wierszy w ramce danych `pandas.DataFrame`). Celem jest upewnienie się, że Matplotlib potrafi zagregować i wyrenderować obiekty bez błędu `MemoryError` i w czasie akceptowalnym dla użytkownika (< 45.0s).

**Otrzymane Wyniki Statystyczne:**
* **Najszybszy czas (Min):** 0.5133 s  <- Najlepszy scenariusz dla procesora s
* **Najwolniejszy (Max):** 0.5350 s  <- Uwzględnia spowolnienia systemu (czkawki) s
* **Średni czas (Mean):** 0.5217 s  <- Średnia arytmetyczna wydajności s
* **Typowy czas (Mediana):** 0.5208 s  <- Wartość środkowa (odporna na anomalie systemu) s
* **Przepustowość:** 2,875,128 pkt/s <- Tyle punktów Seaborn rysuje w 1 sekundę!

**Wnioski:** Test zakończony sukcesem. System poradził sobie z trzykrotnym obciążeniem względem wstępnych założeń z dokumentacji. Czas generowania wykresu jest wprost proporcjonalny do ilości danych, jednak Seaborn zachowuje stabilność.

---

## Scenariusz 2: Złożoność Grupowania (Kardynalność 'hue')
**Plik testowy:** `tests/test_performance_hue.py`

**Opis testu:** Weryfikacja narzutu obliczeniowego podczas korzystania z wizualnej parametryzacji `hue`. Wygenerowano 200 000 wierszy i wymuszono podział na **250 unikalnych kategorii**. Wymaga to od Seaborna wykonania ciężkich operacji w grupowaniu danych, a od Matplotliba alokacji palet dla 250 oddzielnych kolekcji.

**Otrzymane Wyniki Statystyczne:**
* **Najszybszy czas (Min):** 1.9129 s s
* **Najwolniejszy (Max):**  2.1081 s s
* **Średni czas (Mean):** 1.9915 s s
* **Typowy czas (Mediana):** 1.9554 s s
* **Szybkość grupowania:**    100,425 pkt/s <- Wpływ przypisywania 250 kolorów s s

**Wnioski:** Narzut obliczeniowy na operacje grupujące Pandas i dynamiczne mapowanie kolorów drastycznie wpływa na przepustowość względem "czystego" wykresu punktowego. Limit akceptacyjny (30.0s) nie został jednak przekroczony.
