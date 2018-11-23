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


    def getMinAndMaxRowLenght(self, array):

        lenghts = [len(arr) for arr in array]
        return min(lenghts), max(lenghts)


    def equalListToLen(self, array, lenght):

        return [arr[0:lenght] for arr in array]


    # def equalListToLen2(self, array1, array2, lenght):
    #
    #     return [arr1[0:lenght] for arr1 in array1], [arr2[0:lenght] for arr2 in array2]


    def computeCenters(self, dataDict):

        centers = []
        labels = []
        for key in dataDict.keys():

            minLen, maxLen = self.getMinAndMaxRowLenght(dataDict[key])

            if(minLen != maxLen):

                dataDict[key] = self.equalListToLen(dataDict[key], minLen)

            dataDict[key] = np.array(dataDict[key])
            mean = dataDict[key].mean(axis=0)
            centers.append(mean)
            labels.append(key)

        minLen, maxLen = self.getMinAndMaxRowLenght(centers)
        if(minLen != maxLen): centers = self.equalListToLen(centers, minLen)

        return np.array(centers), np.array(labels)


    def PredictLabel(self, sample):

        centers = self.centers
        if(len(sample) < len(self.centers[0])):

            centers = np.array([center[0:len(sample)] for center in self.centers])

        else:

            sample = np.array(sample[0:len(self.centers[0])])

        differences = (centers - sample)
        distances = np.einsum('ij, ij->i', differences, differences)
        nearest = self.labels[np.argsort(distances)[0]]

        return nearest