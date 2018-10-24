from scipy.stats import mode
import numpy as np

class KNN:

    def __init__(self, data, labels, k):
        self.data = data
        self.labels = labels
        self.k = k

    def predict(self, sample):
        differences = (self.data - sample)
        distances = np.einsum('ij, ij->i', differences, differences)
        nearest = self.labels[np.argsort(distances)[:self.k]]
        return mode(nearest)[0][0]
