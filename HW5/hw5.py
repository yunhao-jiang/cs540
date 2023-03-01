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
        vector = np.array([[1, year]])
        X = np.concatenate((X, vector), axis=0)
    return X


def q3b():
    return np.array(days)


def q3c(X):
    """compute X^T * X"""
    return np.dot(X.T, X)


def q3d(Z):
    """compute (X^T * X)^-1"""
    return np.linalg.inv(Z)


def q3e(I):
    """compute (X^T * X)^-1 * X^T"""
    return np.dot(I, X.T)


def q3f():
    """compute (X^T * X)^-1 * X^T * Y"""
    return np.dot(PI, Y)


def q4(x):
    return hat_beta[0] + hat_beta[1] * x


def q5(hat_beta):
    if hat_beta[1] < 0:
        return "<", "decreasing"
    elif hat_beta[1] > 0:
        return ">", "increasing"
    else:
        return "=", "constant"


def q6(hat_beta):
    """compute 0 = hat_beta[0] + hat_beta[1] * x, what is x?"""
    return -hat_beta[0] / hat_beta[1]


file_name = sys.argv[1]
with open(file_name, 'r') as file:
    load_visualize(file)
    print("Q3a:")
    X = q3a()
    print(X)

    print("Q3b:")
    Y = q3b()
    print(Y)

    print("Q3c:")
    Z = q3c(X)
    print(Z)

    print("Q3d:")
    I = q3d(Z)
    print(I)

    print("Q3e:")
    PI = q3e(I)
    print(PI)

    print("Q3f:")
    hat_beta = q3f()
    print(hat_beta)

    y_test = q4(2022)
    print("Q4: " + str(y_test))

    q5a, q5b = q5(hat_beta)
    print("Q5a: " + q5a)
    print("Q5b: The number of frozen days on Lake Mendota is " + q5b + ".")

    q6a = q6(hat_beta)
    print("Q6a: " + str(q6a))
    print("Q6b: x is not compelling because the dataset is too small.")
