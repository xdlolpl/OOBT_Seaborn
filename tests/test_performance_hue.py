import pytest
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
import statistics

# Kody ANSI do kolorowania tekstu w terminalu
C_RESET = "\033[0m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_BLUE = "\033[94m"
C_CYAN = "\033[96m"
C_BOLD = "\033[1m"

# Wyłączenie renderowania okienek z wykresami (kluczowe w osobnym pliku!)
plt.switch_backend('Agg')


@pytest.fixture
def complex_hue_dataset():
    """Fixtura dostarczająca zbiór danych o wysokiej kardynalności do testowania parametru hue."""
    rows = 200_000
    num_categories = 250  # 250 unikalnych grup/kolorów do przetworzenia!
    df = pd.DataFrame({
        'x': np.random.rand(rows),
        'y': np.random.rand(rows),
        # Generujemy losowe kategorie od 0 do 249
        'kategoria': np.random.randint(0, num_categories, size=rows)
    })
    return df, rows, num_categories


def test_hue_cardinality_performance(complex_hue_dataset):
    df, rows_count, num_categories = complex_hue_dataset

    # 1. Kolorowy Nagłówek raportu
    print(f"\n{C_CYAN}{C_BOLD}╔══════════════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}║  🎨 ZAAWANSOWANY RAPORT WYDAJNOŚCIOWY: SEABORN 'HUE' OVERHEAD        ║{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}╚══════════════════════════════════════════════════════════════════════╝{C_RESET}")

    print(f"{C_YELLOW}[ℹ️] KONTEKST TESTU:{C_RESET}")
    print(f" ├─ Rozmiar danych: {C_BOLD}{rows_count:,.0f} punktów{C_RESET}")
    print(f" ├─ Kardynalność:   {C_BOLD}{num_categories} unikalnych kategorii (kolorów){C_RESET}")
    print(f" ├─ Środowisko:     Backend 'Agg' (bezokienkowy, wyłączona legenda)")
    print(f" └─ Metodologia:    Rozgrzewka silnika + {C_BOLD}5 iteracji testowych{C_RESET}\n")

    print(f"{C_YELLOW}[❓] DLACZEGO TESTUJEMY PARAMETR 'HUE'?{C_RESET}")
    print(f" ├─ {C_BOLD}Obciążenie Pandasa:{C_RESET} Seaborn musi najpierw pogrupować dane pod spodem.")
    print(f" ├─ {C_BOLD}Alokacja palet:{C_RESET} Silnik musi dynamicznie wygenerować 250 odcieni barw.")
    print(f" └─ {C_BOLD}Cykle Matplotliba:{C_RESET} Zamiast jednego obiektu z punktami, biblioteka musi")
    print(f"    stworzyć 250 oddzielnych warstw (kolekcji) na jednym wykresie.\n")

    print(f"{C_GREEN}[Uruchamianie] Przetwarzanie grup i rysowanie... Proszę czekać.{C_RESET}\n")

    def render_plot():
        # Wyłączamy legendę, ponieważ generowanie legendy z 250 elementami zablokowałoby test
        ax = sns.scatterplot(data=df, x='x', y='y', hue='kategoria', legend=False, palette="viridis")
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
    print(f"{C_BLUE}{C_BOLD}│ ⏱️  SZCZEGÓŁOWE WYNIKI ITERACJI (ZŁOŻONOŚĆ HUE)                       │{C_RESET}")
    print(f"{C_BLUE}{C_BOLD}├──────────────┬───────────────────────────────────────────────────────┤{C_RESET}")
    print(f"{C_BLUE}{C_BOLD}│ Iteracja     │ Czas wykonania                                        │{C_RESET}")
    print(f"{C_BLUE}{C_BOLD}├──────────────┼───────────────────────────────────────────────────────┤{C_RESET}")
    for i, czas in enumerate(czasy_wykonania, 1):
        kolor_czasu = C_GREEN if czas <= sredni else C_YELLOW
        print(f"│ Test #{i:<6} │ {kolor_czasu}{czas:>7.4f} sekund{C_RESET}                                      │")
    print(f"{C_BLUE}{C_BOLD}└──────────────┴───────────────────────────────────────────────────────┘{C_RESET}\n")

    # 6. Słowniczek i analiza statystyczna
    print(f"{C_CYAN}{C_BOLD}╔══════════════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}║ 📊 PODSUMOWANIE STATYSTYCZNE: NARZUT GRUPOWANIA                      ║{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}╠══════════════════════════════════════════════════════════════════════╣{C_RESET}")
    print(f" {C_BOLD}Najszybszy czas (Min):{C_RESET}  {C_GREEN}{najkrotszy:>7.4f} s{C_RESET}")
    print(f" {C_BOLD}Najwolniejszy (Max):{C_RESET}    {C_RED}{najdluzszy:>7.4f} s{C_RESET}")
    print(f" {C_BOLD}Średni czas (Mean):{C_RESET}     {C_CYAN}{sredni:>7.4f} s{C_RESET}")
    print(f" {C_BOLD}Typowy czas (Mediana):{C_RESET}  {C_CYAN}{mediana:>7.4f} s{C_RESET}")
    print(
        f" {C_BOLD}Stabilność (StdDev):{C_RESET}    {odchylenie:>7.4f} s  {C_YELLOW}<- Skoki oznaczają trudności z alokacją{C_RESET}")
    print(
        f" {C_BOLD}Szybkość grupowania:{C_RESET}    {przepustowosc:>7,.0f} pkt/s {C_YELLOW}<- Wpływ przypisywania 250 kolorów{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}╚══════════════════════════════════════════════════════════════════════╝{C_RESET}\n")

    # 7. Ostateczna asercja
    limit_sekund = 30.0
    assert sredni < limit_sekund, f"Wydajność zbyt niska! Średni czas {sredni:.2f}s przekracza limit {limit_sekund}s."