from scipy.stats import mode
import numpy as np

class KNN:

    def __init__(self, data, labels, k):

        if(type(data) == str):

            dataFileName = "Output\\" + data
            labelsFileName = "Output\\" + labels
            self.data, self.labels = self.readTrainData(dataFileName, labelsFileName)

        else:

            self.data = data
            self.labels = labels

        self.k = k


    def readTrainData(self, dataFileName, labelFileName):

        trainData = None
        trainLabels = None

        with open(dataFileName) as df, open(labelFileName) as lf:

            all_data = df.readlines()
            all_labels = lf.readlines()
            trainData = [[float(val) for val in line.split()] for line in all_data]
            trainLabels = [line.split("\n")[0] for line in all_labels]

        return np.array(trainData), np.array(trainLabels)


    def predict(self, sample):

        differences = (self.data - sample)
        distances = np.einsum('ij, ij->i', differences, differences)
        nearest = self.labels[np.argsort(distances)[:self.k]]
        return mode(nearest)[0][0]
