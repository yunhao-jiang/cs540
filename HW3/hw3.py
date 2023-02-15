from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt


def load_and_center_dataset(filename):
    """load the dataset from the provided.npyfile, center it around the origin, and return it as
    a numpy array of floats."""
    dataset = np.load(filename)
    dataset = dataset.astype(float)
    dataset = dataset - np.mean(dataset, axis=0)
    return dataset


def get_covariance(dataset):
    """calculate and return the covariance matrix of the dataset as a numpy matrix (d×d array)."""
    # return np.cov(dataset)
    return np.dot(np.transpose(dataset), dataset) / (len(dataset) - 1)


def get_eig(S, m):
    """perform eigendecomposition on the covariance matrix S and return a diagonal matrix (numpy
    array) with the largest m eigenvalues on the diagonal in descending order, and a matrix (
    numpy array) with the corresponding eigenvectors as columns. """
    w, v = eigh(S, subset_by_index=(len(S) - m, len(S) - 1))
    return np.diag(w[::-1]), v[:, ::-1]


def get_eig_prop(S, prop):
    """similar to get_eig, but instead of returning the first m, return all eigen- values and
    corresponding eigenvectors in a similar format that explain more than a prop proportion of
    the variance (specifically, please make sure the eigenvalues are returned in descending
    order). """
    sum = 0
    for i in range(0, len(S)):
        sum += S[i][i]
    w, v = eigh(S, subset_by_value=(sum * prop, np.inf))
    return np.diag(w[::-1]), v[:, ::-1]


def project_image(image, U):
    """project the image into the m-dimensional subspace and then project back into d × 1
    dimensions and return that """
    return np.dot(np.dot(U, np.transpose(U)), image)


def display_image(orig, proj):
    """use matplotlib to display a visual representation of the original image and the projected
    image side-by-side with colorbar """
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('Original')
    img1 = ax1.imshow(np.transpose(orig.reshape(32, 32)), aspect='equal')
    fig.colorbar(img1, ax=ax1)

    ax2.set_title('Projection')
    img2 = ax2.imshow(np.transpose(proj.reshape(32, 32)), aspect='equal')
    fig.colorbar(img2, ax=ax2)

    plt.show()


x = load_and_center_dataset('YaleB_32x32.npy')
S = get_covariance(x)
Lambda, U = get_eig(S, 2)
projection = project_image(x[0], U)
display_image(x[0], projection)
