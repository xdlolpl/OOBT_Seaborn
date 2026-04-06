import pytest
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def test_scatterplot_data_bounds():
    # 1. Ładujemy wbudowany zbiór danych Seaborna
    tips = sns.load_dataset("tips")
    
    # 2. Tworzymy wykres
    ax = sns.scatterplot(data=tips, x="total_bill", y="tip")
    
    # 3. WERYFIKACJA GŁĘBOKA:
    # Sprawdzamy, czy nazwy osi automatycznie ustawiły się na nazwy kolumn
    assert ax.get_xlabel() == "total_bill"
    assert ax.get_ylabel() == "tip"
    
    # Sprawdzamy, czy zakres osi X obejmuje nasze dane
    # (czy największa wartość rachunku mieści się w widocznym zakresie)
    x_limit_max = ax.get_xlim()[1]
    assert x_limit_max >= tips["total_bill"].max(), "Wykres ucina dane na osi X!"
    
    plt.close()

def test_countplot_order_integrity():
    # Sprawdzamy, czy kolejność słupków na wykresie zgadza się z naszym zamówieniem
    df = pd.DataFrame({"dni": ["Pon", "Wt", "Śr", "Pon", "Pon", "Wt"]})
    porzadek = ["Pon", "Wt", "Śr"]
    
    ax = sns.countplot(data=df, x="dni", order=porzadek)
    
    # Wyciągamy etykiety z osi X
    labels = [label.get_text() for label in ax.get_xticklabels()]
    
    # Sprawdzamy, czy kolejność na wykresie jest dokładnie taka, jaką zadaliśmy
    assert labels == porzadek, "Kolejność słupków na wykresie jest niepoprawna!"
    
    plt.close()