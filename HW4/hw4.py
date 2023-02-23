import csv
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt


def get_dist_matrix(data):
    """Calculate the distance matrix for the given data."""
    # Referenced https://jaykmody.com/blog/distance-matrices-with-numpy/
    dist_matrix = np.zeros((len(data), len(data)))
    for i in range(len(data)):
        for j in range(len(data)):
            if j == i:
                dist_matrix[i][j] = 0  # Diagonal is 0, skip calculation
            elif j < i:
                dist_matrix[i][j] = dist_matrix[j][i]  # Symmetric matrix, skip calculation
            else:
                dist_matrix[i][j] = np.sqrt(np.sum((data[i] - data[j]) ** 2))  # Euclidean distance
    return dist_matrix


def load_data(filepath):
    """Return a list of dictionaries, where each row in the dataset is a dictionary with
    the column headers as keys and the row elements as values. """
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data


def calc_features(row):
    """Return Attack, Sp. Atk, Speed, Defense, Sp. Def, and HP as a numpy array."""
    return np.array([row['Attack'], row['Sp. Atk'], row['Speed'], row['Defense'], row['Sp. Def'],
                     row['HP']]).astype(int)


def larger_one(x, y):
    """Return the larger one of x and y."""
    if x > y:
        return x
    else:
        return y


def hac(features):
    """numpy array of shape (n − 1) × 4."""
    # Set up
    dist_matrix = get_dist_matrix(features)
    Z = np.zeros((len(features) - 1, 4))
    clusters = np.arange(len(features))
    dict_num_in_cluster = {i: 1 for i in range(len(features))}  # keep track of # of pokemon

    for i in range(len(features) - 1):
        # Find the two clusters with the smallest distance
        min_dist = np.inf
        min_cluster_index = None
        cluster_num = None
        for j in range(len(clusters)):
            for k in range(j + 1, len(clusters)):
                dist = np.max(dist_matrix[clusters[j], clusters[k]])
                if dist < min_dist:
                    min_dist = dist
                    min_cluster_index = (j, k)
                    cluster_num = (clusters[j], clusters[k])

        # Save the information in Z
        Z[i, 0] = min(cluster_num)
        Z[i, 1] = max(cluster_num)
        Z[i, 2] = min_dist
        Z[i, 3] = dict_num_in_cluster[cluster_num[0]] + dict_num_in_cluster[cluster_num[1]]
        dict_num_in_cluster[len(features) + i] = int(Z[i, 3])

        # Merge the two clusters
        clusters = np.delete(clusters, min_cluster_index)
        clusters = np.append(clusters, len(features) + i)

        # Expand the distance matrix for the new cluster
        new_row = np.zeros((1, len(dist_matrix)))
        new_col = np.zeros((len(dist_matrix) + 1, 1))
        dist_matrix = np.append(dist_matrix, new_row, axis=0)
        dist_matrix = np.append(dist_matrix, new_col, axis=1)
        for j in range(len(dist_matrix) - 1):
            dist_matrix[-1, j] = larger_one(dist_matrix[cluster_num[0], j], dist_matrix[
                cluster_num[1], j])
            dist_matrix[j, -1] = dist_matrix[-1, j]

    return Z


def imshow_hac(Z, names):
    """Plot the dendrogram."""
    plt.subplot(1, 1, 1)
    plt.title(f'N = {len(names)}')
    hierarchy.dendrogram(Z, labels=names, leaf_rotation=90)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    features_and_names = [(calc_features(row), row['Name']) for row in
                          load_data('Pokemon.csv')[:10]]
    Z = hac([row[0] for row in features_and_names])
    imshow_hac(Z, [row[1] for row in features_and_names])
