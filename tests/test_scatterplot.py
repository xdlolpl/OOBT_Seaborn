
import pytest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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