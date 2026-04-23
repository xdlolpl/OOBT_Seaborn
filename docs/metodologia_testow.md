# Metodologia Testowania Projektu OOB Seaborn

Dokument opisuje kompleksowe podejście zespołu do zapewnienia jakości (QA) biblioteki Seaborn, realizowane w ramach projektu "out-of-the-box". Nasza strategia opiera się na wielopoziomowym testowaniu, od weryfikacji potrzeb użytkownika po zabezpieczenie stabilności systemu.

## 1. Testy Akceptacyjne (Perspektywa Użytkownika)
Zgodnie z dobrymi praktykami inżynierii oprogramowania, proces testowania rozpoczęliśmy od zdefiniowania wymagań użytkownika. Testy akceptacyjne odpowiadają na pytanie: "czy użytkownik osiąga swój cel?", a nie "jak technicznie zaimplementowana jest funkcja?".
Zdefiniowaliśmy 5 kluczowych scenariuszy (TS_01 - TS_05), w tym m.in. poprawne generowanie wykresu punktowego oraz zachowanie systemu w przypadku braków danych (NaN). Każdy scenariusz posiada jasne warunki początkowe, kroki oraz oczekiwany rezultat. Wszystkie nasze testy akceptacyjne zostały w 100% zautomatyzowane.

## 2. Testy Regresyjne (Strażnik Stabilności)
Testy regresji to nasz mechanizm obronny przed sytuacją, w której zmiana w kodzie lub aktualizacja biblioteki psuje wcześniej działające funkcje. W naszym projekcie **każdy test zautomatyzowany uruchamiany w CI/CD pełni rolę testu regresyjnego**. 
Regresja w naszym rozumieniu to nie tylko błędy typu crash (np. zła nazwa kolumny testowana w `test_scatterplot_invalid_column`), ale również pogorszenie wydajności. Dlatego nasze testy wydajnościowe również wchodzą w skład zestawu regresyjnego. Złota zasada, którą się kierujemy to: „Naprawiając jedno - nie psuj drugiego".

## 3. Testy Integracyjne i Systemowe
Ponieważ Seaborn jest biblioteką opartą na Matplotlib i ściśle współpracującą ze strukturami danych Pandas i Numpy, większość naszych testów ma charakter integracyjny. Sprawdzają one współpracę komponentów:
* `pandas` dostarcza i formatuje dane (np. kategoryzacja do parametru `hue` sprawdzana w `test_scatterplot_hue_parameter`).
* `seaborn` odpowiada za obliczenia statystyczne i mapowanie wizualne.
* `matplotlib` (używamy backendu `Agg`, aby zapobiec problemom z biblioteką tkinter w CI/CD) ostatecznie renderuje obiekt `Axes`.
Błędy wykrywane na tym poziomie to m.in. problemy z przepływem danych między bibliotekami.

## 4. Automatyzacja (CI/CD)
Zgodnie z zasadą, że testy regresji mają sens tylko wtedy, gdy są szybkie, automatyczne i powtarzalne, uruchamiamy je poprzez narzędzie `pytest` w ramach GitHub Actions (konfiguracja: Hubert Miłuch). Wykorzystujemy m.in. dekoratory `@pytest.mark.parametrize` do sprawnego testowania wielu zmiennych (np. palet kolorów czy typów wykresów) w ramach pojedynczego bloku kodu.
