from calculator import dodawanie,dzielenie,mnozenie,odejmowanie, create_dataset, get_mean_price, get_blue_cars,get_doors_count
import pandas as pd
def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(-1, 1) == 0

def test_odejmowanie():
    assert odejmowanie(5, 3) == 2
    assert odejmowanie(1, -1) == 2

def test_mnozenie():
    assert mnozenie(2, 3) == 6
    assert mnozenie(-1, 1) == -1

def test_dzielenie():
    assert dzielenie(6, 3) == 2
    assert dzielenie(1, -1) == -1
    assert dzielenie(1, 0) == "Błąd: dzielenie przez zero!"

dataset = {
    'cars': ['Audi', 'BMW', 'Peugeot', 'Ford'],
    'color': ['red', 'black', 'blue', 'blue'],
    'doors': [5,3,5,5],
    'price': [6000,4500, 3000, 6500]
}

def test_create_dataset():
    data = create_dataset(dataset)
    assert data.shape == (4,4)
    assert data.size == 16

def test_get_mean_price():
    data = create_dataset(dataset)
    mean = get_mean_price(data)
    assert mean != -1
    assert mean == 5000

def test_get_blue_cars():
    data = create_dataset(dataset)
    expected = pd.DataFrame({
        'cars': ['Peugeot', 'Ford'],
        'price': [3000, 6500]
    })
    result = get_blue_cars(data)
    assert result.reset_index(drop=True).equals(expected.reset_index(drop=True))

def test_get_doors_count():
    data = create_dataset(dataset)
    assert get_doors_count(data) == 18
