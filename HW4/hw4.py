import csv
import numpy as np


def load_data(filepath):
    """Return a list of dictionaries, where each row in the dataset is a dictionary with
    the column headers as keys and the row elements as values. """
    with open(filepath) as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data


def calc_features(row):
    """Return Attack, Sp. Atk, Speed, Defense, Sp. Def, and HP as a numpy array."""
    return np.array([row['Attack'], row['Sp. Atk'], row['Speed'], row['Defense'], row['Sp. Def'],
                     row['HP']]).astype(int)


def hac(features):
    pass


def imshow_hac(Z, names):
    pass


if __name__ == '__main__':
    data = load_data('Pokemon.csv')
    print(calc_features(data[0]))
