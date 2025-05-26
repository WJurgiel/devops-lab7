import numpy as np
import pandas as pd

def dodawanie(liczba1, liczba2):
    return np.add(liczba1, liczba2)

def odejmowanie(liczba1, liczba2):
    return np.subtract(liczba1, liczba2)

def mnozenie(liczba1, liczba2):
    return np.multiply(liczba1, liczba2)

def dzielenie(liczba1, liczba2):
    if liczba2 != 0:
        return np.divide(liczba1, liczba2)
    else:
        return "Błąd: dzielenie przez zero!"

def power_of_two(number):
    return number ** 2

def create_dataset(dataset):
    data = pd.DataFrame(dataset)
    return data

def get_mean_price(data):
    if 'price' in data.columns: 
        return data.price.mean()
    return -1

def get_blue_cars(data):
    if 'color' and 'cars' in data.columns:
        return data[data['color'] == 'blue'][['cars', 'price']]
    return -1

def get_doors_count(data):
    return sum(data['doors'])
