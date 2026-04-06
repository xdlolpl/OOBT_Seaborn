import pytest
import pandas as pd

# Dekorator @pytest.fixture mówi Pytestowi: "To jest dawca danych"
@pytest.fixture
def sample_data():
    # Zamiast kopiować te dane do każdego testu, definiujemy je raz tutaj
    return pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 15, 13, 20, 18],
        'kategoria': ['A', 'A', 'B', 'B', 'C']
    })