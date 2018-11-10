import numpy as np

class OtoczKul:

    def __init__(self, dataFileName, labelsFileName):

        dataFileName = "Output\\" + dataFileName
        labelsFileName = "Output\\" + labelsFileName
        data, labels = self.readTrainData(dataFileName, labelsFileName)
        dataDict = self.storeAsDict(data, labels)
        self.centers, self.labels = self.computeCenters(dataDict)


    def readTrainData(self, dataFileName, labelFileName):

        trainData = None
        trainLabels = None

        with open(dataFileName) as df, open(labelFileName) as lf:

            all_data = df.readlines()
            all_labels = lf.readlines()
            trainData = [[float(val) for val in line.split()] for line in all_data]
            trainLabels = [line.split("\n")[0] for line in all_labels]

        return trainData, trainLabels


    def storeAsDict(self, data, labels):

        dict = {}
        for i in range(len(labels)):

            if(labels[i] not in dict.keys()):

                dict[labels[i]] = []

            dict[labels[i]].append(data[i])

        return dict


    def computeCenters(self, dataDict):

        centers = []
        labels = []
        for key in dataDict.keys():

            dataDict[key] = np.array(dataDict[key])
            centers.append(dataDict[key].mean(axis=0))
            labels.append(key)

        return np.array(centers), np.array(labels)


    def PredictLabel(self, sample):

        differences = (self.centers - sample)
        distances = np.einsum('ij, ij->i', differences, differences)
        nearest = self.labels[np.argsort(distances)[0]]

        return nearest