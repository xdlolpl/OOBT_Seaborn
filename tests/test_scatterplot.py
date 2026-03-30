
import pytest
import pandas as pd

import matplotlib
matplotlib.use('Agg') # <-- TA LINIJKA NAPRAWIA BŁĄD Z TKINKEREM
import matplotlib.pyplot as plt
import seaborn as sns


def test_scatterplot_happy_path():
    # 1. Przygotowanie testowych danych (Arrange)
    df = pd.DataFrame({
        'total_bill': [10.0, 15.5, 20.0],
        'tip': [1.5, 2.0, 3.5]
    })

    # 2. Wykonanie akcji - rysowanie wykresu (Act)
    ax = sns.scatterplot(data=df, x='total_bill', y='tip')

    # 3. Weryfikacja (Assert)
    assert ax is not None, "Wykres nie został utworzony"
    assert ax.get_xlabel() == 'total_bill', "Nieprawidłowa etykieta osi X"
    assert ax.get_ylabel() == 'tip', "Nieprawidłowa etykieta osi Y"
    assert len(ax.collections) > 0, "Brak punktów na wykresie"

    
    # 4. Sprzątanie
    plt.close()


def test_scatterplot_invalid_column():
    # 1. Przygotowanie danych (tylko jedna poprawna kolumna)
    df = pd.DataFrame({
        'poprawna_nazwa': [1, 2, 3]
    })

    # 2 & 3. Wykonanie i Weryfikacja (oczekujemy błędu KeyError)
    with pytest.raises(ValueError):
        sns.scatterplot(data=df, x='poprawna_nazwa', y='literowka_w_nazwie')

def test_scatterplot_hue_parameter():
    # 1. Przygotowanie danych (dodajemy kolumnę z kategoriami)
    df = pd.DataFrame({
        'oś_x': [1, 2, 3, 4],
        'oś_y': [10, 20, 15, 25],
        'kategoria': ['Grupa A', 'Grupa A', 'Grupa B', 'Grupa B']
    })

    # 2. Wykonanie akcji - rysowanie z podziałem na kolory
    ax = sns.scatterplot(data=df, x='oś_x', y='oś_y', hue='kategoria')

    # 3. Weryfikacja
    assert ax is not None, "Wykres nie został utworzony"
    
    # Skoro użyliśmy 'hue', Seaborn musiał wygenerować legendę dla kolorów.
    # Sprawdzamy, czy legenda faktycznie istnieje na wykresie.
    assert ax.get_legend() is not None, "Brak legendy na wykresie z parametrem hue"

    # 4. Sprzątanie pamięci
    plt.close()