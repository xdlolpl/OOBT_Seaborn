import pytest
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def test_reproducer_mismatched_lengths():
    """
    REPRODUCER: Weryfikacja błędu przy asymetrycznych danych wejściowych.
    Cel: Udowodnienie, że Seaborn przerywa rysowanie i rzuca konkretny
    wyjątek (ValueError), gdy tablice osi X i Y mają różną długość.
    """
    # 1. Dane wejściowe (Asymetryczne)
    x_data = [1, 2, 3]       # Długość 3
    y_data = [10, 20]        # Długość 2 (brakuje jednego elementu!)

    # 2. Wywołanie i weryfikacja
    # Oczekujemy, że system rzuci błąd i nie wygeneruje wykresu
    with pytest.raises(ValueError) as excinfo:
        sns.scatterplot(x=x_data, y=y_data)
    
    # 3. Sprawdzenie, czy błąd to faktycznie problem z długością danych
    # (Przechwytujemy komunikat rzucony przez bibliotekę pod spodem)
    assert "length" in str(excinfo.value).lower() or "match" in str(excinfo.value).lower(), \
        f"Nieoczekiwany komunikat błędu: {excinfo.value}"
        
    plt.close()