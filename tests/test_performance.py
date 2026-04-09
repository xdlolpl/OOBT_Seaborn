import pytest
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
import statistics







# Aby uruchomić poprawnie test należy wkleic w terminal tą komende: pytest -s test_performance.py








# Kody ANSI do kolorowania tekstu w terminalu
C_RESET = "\033[0m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_BLUE = "\033[94m"
C_CYAN = "\033[96m"
C_BOLD = "\033[1m"

# Wyłączenie renderowania okienek z wykresami.
plt.switch_backend('Agg')


@pytest.fixture
def large_dataset():
    """Fixtura dostarczająca ekstremalnie duży zbiór danych (1.5 miliona wierszy)."""
    rows = 1_500_000
    df = pd.DataFrame({
        'x': np.random.rand(rows),
        'y': np.random.rand(rows)
    })
    return df, rows


def test_scatterplot_performance_large_data(large_dataset):
    df, rows_count = large_dataset

    # 1. Kolorowy Nagłówek raportu
    print(f"\n{C_CYAN}{C_BOLD}╔══════════════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}║  🚀 ZAAWANSOWANY RAPORT WYDAJNOŚCIOWY: SEABORN SCATTERPLOT 🚀        ║{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}╚══════════════════════════════════════════════════════════════════════╝{C_RESET}")

    print(f"{C_YELLOW}[ℹ️] KONTEKST TESTU:{C_RESET}")
    print(f" ├─ Rozmiar danych: {C_BOLD}{rows_count:,.0f} punktów{C_RESET} (Trzykrotne obciążenie!)")
    print(f" ├─ Środowisko:     Backend 'Agg' (bezokienkowy)")
    print(f" └─ Metodologia:    Rozgrzewka silnika + {C_BOLD}5 iteracji testowych{C_RESET}\n")

    # --- NOWA SEKCJA Z WYJAŚNIENIEM ---
    print(f"{C_YELLOW}[❓] DLACZEGO WYKONUJEMY AŻ 5 ITERACJI?{C_RESET}")
    print(f" ├─ {C_BOLD}Anomalie sprzętowe:{C_RESET} System operacyjny często wykonuje nagłe procesy w tle")
    print(f" │  (np. antywirus, aktualizacje), które mogą sztucznie zawyżyć czas jednego pomiaru.")
    print(f" ├─ {C_BOLD}Zarządzanie pamięcią:{C_RESET} Automatyczne odśmiecanie pamięci (Garbage Collector)")
    print(f" │  w Pythonie może włączyć się w losowym momencie i spowolnić pojedynczy cykl.")
    print(f" └─ {C_BOLD}Wiarygodność statystyczna:{C_RESET} Obliczenie Mediany i Średniej z kilku prób odrzuca")
    print(f"    skrajne piki systemowe, dając nam rzetelny i powtarzalny wynik.\n")
    # ----------------------------------

    print(f"{C_GREEN}[Uruchamianie] Trwa rysowanie wykresów... Proszę czekać.{C_RESET}\n")

    # Zdefiniowanie operacji rysowania
    def render_plot():
        ax = sns.scatterplot(data=df, x='x', y='y')
        return ax

    # 2. Faza rozgrzewki
    render_plot()
    plt.close('all')

    # 3. Pomiary właściwe
    czasy_wykonania = []
    liczba_iteracji = 5

    for i in range(liczba_iteracji):
        start_czas = time.perf_counter()

        wynikowy_wykres = render_plot()

        koniec_czas = time.perf_counter()
        czasy_wykonania.append(koniec_czas - start_czas)

        assert wynikowy_wykres is not None
        plt.close('all')

    # 4. Zaawansowane obliczenia statystyczne
    najkrotszy = min(czasy_wykonania)
    najdluzszy = max(czasy_wykonania)
    sredni = statistics.mean(czasy_wykonania)
    mediana = statistics.median(czasy_wykonania)
    odchylenie = statistics.stdev(czasy_wykonania)
    przepustowosc = rows_count / sredni

    # 5. Rysowanie tabeli
    print(f"{C_BLUE}{C_BOLD}┌──────────────────────────────────────────────────────────────────────┐{C_RESET}")
    print(f"{C_BLUE}{C_BOLD}│ ⏱️  SZCZEGÓŁOWE WYNIKI ITERACJI                                       │{C_RESET}")
    print(f"{C_BLUE}{C_BOLD}├──────────────┬───────────────────────────────────────────────────────┤{C_RESET}")
    print(f"{C_BLUE}{C_BOLD}│ Iteracja     │ Czas wykonania                                        │{C_RESET}")
    print(f"{C_BLUE}{C_BOLD}├──────────────┼───────────────────────────────────────────────────────┤{C_RESET}")
    for i, czas in enumerate(czasy_wykonania, 1):
        kolor_czasu = C_GREEN if czas <= sredni else C_YELLOW
        print(f"│ Test #{i:<6} │ {kolor_czasu}{czas:>7.4f} sekund{C_RESET}                                      │")
    print(f"{C_BLUE}{C_BOLD}└──────────────┴───────────────────────────────────────────────────────┘{C_RESET}\n")

    # 6. Słowniczek i analiza statystyczna
    print(f"{C_CYAN}{C_BOLD}╔══════════════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}║ 📊 PODSUMOWANIE STATYSTYCZNE I ANALIZA WYNIKÓW                       ║{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}╠══════════════════════════════════════════════════════════════════════╣{C_RESET}")
    print(
        f" {C_BOLD}Najszybszy czas (Min):{C_RESET}  {C_GREEN}{najkrotszy:>7.4f} s{C_RESET}  {C_YELLOW}<- Najlepszy scenariusz dla procesora{C_RESET}")
    print(
        f" {C_BOLD}Najwolniejszy (Max):{C_RESET}    {C_RED}{najdluzszy:>7.4f} s{C_RESET}  {C_YELLOW}<- Uwzględnia spowolnienia systemu (czkawki){C_RESET}")
    print(
        f" {C_BOLD}Średni czas (Mean):{C_RESET}     {C_CYAN}{sredni:>7.4f} s{C_RESET}  {C_YELLOW}<- Średnia arytmetyczna wydajności{C_RESET}")
    print(
        f" {C_BOLD}Typowy czas (Mediana):{C_RESET}  {C_CYAN}{mediana:>7.4f} s{C_RESET}  {C_YELLOW}<- Wartość środkowa (odporna na anomalie systemu){C_RESET}")
    print(
        f" {C_BOLD}Stabilność (StdDev):{C_RESET}    {odchylenie:>7.4f} s  {C_YELLOW}<- Im niżej, tym testy są bardziej powtarzalne{C_RESET}")
    print(
        f" {C_BOLD}Przepustowość:{C_RESET}          {przepustowosc:>7,.0f} pkt/s {C_YELLOW}<- Tyle punktów Seaborn rysuje w 1 sekundę!{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}╚══════════════════════════════════════════════════════════════════════╝{C_RESET}\n")

    # 7. Ostateczna asercja
    limit_sekund = 45.0
    assert sredni < limit_sekund, f"Wydajność zbyt niska! Średni czas {sredni:.2f}s przekracza limit {limit_sekund}s."