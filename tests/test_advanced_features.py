import pytest
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Testowanie wielu palet kolorów jednym testem!
# Pytest automatycznie odpali tę funkcję 4 razy, za każdym razem podmieniając 'palette_name'
@pytest.mark.parametrize("palette_name", ["deep", "pastel", "dark", "colorblind"])
def test_scatterplot_multiple_palettes(palette_name):
    df = pd.DataFrame({
        'x': [1, 2, 3], 
        'y': [10, 20, 15], 
        'grupa': ['A', 'B', 'C']
    })
    
    # Wykorzystujemy podmienianą paletę kolorów
    ax = sns.scatterplot(data=df, x='x', y='y', hue='grupa', palette=palette_name)
    
    assert ax is not None, f"Wykres nie powstał dla palety {palette_name}"
    assert len(ax.collections) > 0, "Punkty nie zostały narysowane"
    plt.close()


# 2. Testowanie różnych typów wykresów z użyciem jednej pętli (Deep Dive)
# Sprawdzamy, czy ramka danych pasuje zarówno do wykresu słupkowego, jak i liniowego
@pytest.mark.parametrize("plot_function", [sns.barplot, sns.lineplot])
def test_multiple_chart_types_compatibility(plot_function):
    df = pd.DataFrame({
        'kategoria': ['Poniedziałek', 'Wtorek', 'Środa'],
        'sprzedaż': [150, 200, 180]
    })
    
    # plot_function zachowuje się jak zmienna, która w zależności od testu jest 
    # albo funkcją barplot, albo lineplot!
    ax = plot_function(data=df, x='kategoria', y='sprzedaż')
    
    assert ax is not None, f"Błąd tworzenia wykresu dla funkcji {plot_function.__name__}"
    plt.close()