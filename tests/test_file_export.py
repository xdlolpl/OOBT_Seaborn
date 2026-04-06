import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Zauważ magię: podajemy 'sample_data' jako argument funkcji. 
# Pytest sam znajdzie fixturę o tej nazwie w conftest.py i wstrzyknie tu dane!
def test_save_plot_to_file(sample_data):
    # 1. Rysujemy wykres używając danych wstrzykniętych przez Pytest
    ax = sns.scatterplot(data=sample_data, x='x', y='y', hue='kategoria')
    
    # 2. Zapisujemy do pliku
    file_path = "test_output.png"
    plt.savefig(file_path)
    plt.close()

    # 3. Weryfikacja: sprawdzamy układ plików w systemie (moduł 'os')
    assert os.path.exists(file_path), "Plik graficzny nie został utworzony na dysku!"
    assert os.path.getsize(file_path) > 0, "Utworzony plik jest całkowicie pusty (0 bajtów)!"
    
    # 4. Sprzątanie: usuwamy plik po teście, żeby nie śmiecić w projekcie
    if os.path.exists(file_path):
        os.remove(file_path)