import pytest
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def test_pairgrid_creation():
    """
    Test weryfikujący tworzenie zaawansowanych siatek wielowymiarowych.
    Sprawdza, czy Seaborn potrafi wygenerować macierz wykresów dla całego zbioru.
    """
    # 1. Ładujemy wbudowany zbiór danych 'iris' (klasyk do macierzy)
    iris = sns.load_dataset("iris")
    
    # 2. Tworzymy obiekt siatki (kolorujemy według gatunku)
    g = sns.PairGrid(iris, hue="species")
    
    # 3. Rysujemy różne typy wykresów na przekątnej i poza nią
    g.map_diag(sns.histplot)
    g.map_offdiag(sns.scatterplot)
    
    # 4. Weryfikacja - sprawdzamy czy obiekt siatki faktycznie powstal
    assert g is not None, "Obiekt PairGrid nie został utworzony!"
    
    # Sprawdzamy pod maską Matplotliba, czy wygenerowało się kilka osi (dla siatki)
    assert len(g.axes) > 1, "Siatka nie zawiera odpowiedniej liczby podobszarów (sub-wykresów)"
    
    plt.close('all')