
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
    # 1. Przygotowanie danych (dodajemy kolumnę tekstową z kategoriami)
    df = pd.DataFrame({
        'x': [1, 2, 3, 4],
        'y': [10, 20, 15, 25],
        'kategoria': ['Grupa_A', 'Grupa_B', 'Grupa_A', 'Grupa_B']
    })

    # 2. Wykonanie akcji - rysowanie wykresu z podziałem na kolory (hue)
    ax = sns.scatterplot(data=df, x='x', y='y', hue='kategoria')

    # 3. Weryfikacja (Assert)
    # Sprawdzamy, czy wykres w ogóle wygenerował legendę
    legenda = ax.get_legend()
    assert legenda is not None, "Legenda nie została utworzona, parametr hue mógł nie zadziałać"
    
    # Sprawdzamy, czy tytuł legendy zgadza się z nazwą naszej kolumny
    tytul_legendy = legenda.get_title().get_text()
    assert tytul_legendy == 'kategoria', f"Oczekiwano tytułu 'kategoria', a otrzymano '{tytul_legendy}'"

    # 4. Sprzątanie
    plt.close()


def test_seaborn_theme_change():
    # 1. Zmiana stylu na darkgrid (ciemna siatka)
    sns.set_theme(style="darkgrid")
    
    # 2. Wygenerowanie prostego histogramu
    df = pd.DataFrame({'dane': [1, 2, 2, 3, 3, 3, 4, 4, 5]})
    ax = sns.histplot(data=df, x='dane')
    
    # 3. Weryfikacja
    assert ax is not None, "Wykres nie został utworzony po zmianie stylu"
    # Sprawdzamy pod maską Seaborna, czy siatka w tle jest faktycznie włączona
    assert sns.axes_style()["axes.grid"] == True, "Styl darkgrid powinien mieć włączoną siatkę"
    
    plt.close()

def test_boxplot_empty_dataframe():
    # 1. Przygotowanie całkowicie pustej ramki danych (tylko nazwy kolumn)
    df = pd.DataFrame(columns=['A', 'B'])
    
    # 2. Próba narysowania wykresu pudełkowego dla pustych danych
    ax = sns.boxplot(data=df)
    
    # 3. Weryfikacja - upewniamy się, że funkcja nie zwraca błędu
    assert ax is not None, "Funkcja powinna zwrócić osie, nawet dla pustych danych"
    # Skoro nie ma danych, na wykresie nie powinno być żadnych narysowanych linii (pudełek)
    assert len(ax.lines) == 0, "Wykres dla pustych danych nie powinien mieć narysowanych linii"
    
    plt.close()