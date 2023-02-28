import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

years = []
days = []

def load_visualize(file):
    # draw plot with matplotlib
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        years.append(int(row[0]))
        days.append(int(row[1]))

    plt.plot(years, days)
    plt.xlabel("Year")
    plt.ylabel("Number of frozen days")
    plt.show()


def q3a():
    # vectorize each year into a feature vector
    X = np.array([[]], dtype=int).reshape(0, 2)
    for year in years:
        vector = np.array([[1,year]])
        X = np.concatenate((X, vector), axis=0)
    return X


def q3b():
    return np.array(days)



file_name = "toy.csv"
with open(file_name, 'r') as file:
    load_visualize(file)
    print("Q3a:")
    print(q3a())
    print("Q3b:")
    print(q3b())

