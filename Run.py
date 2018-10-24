import ImageReader as ImReader
import ClassificationDataReader as cdr
import numpy as np
import KNN

# ImReader.saveMnistDataToTxtFile("Images\NumberImages")
trainLabels = cdr.readFileToArray("trainLabelsMnist.csv")
testLabels = cdr.readFileToArray("testLabelsMnist.csv")
trainData = cdr.readFileToArray("trainDataMnist.csv")
testData = cdr.readFileToArray("testDataMnist.csv")

knn = KNN.KNN(trainData, trainLabels, 3)
counter = 0
predictedLabels = []
for sample in testData:
    sample = np.asarray(sample)
    predictedLabels.append(knn.predict(sample))
    if (counter % 100 == 0):
        print counter
    counter += 1
ImReader.createTxtFileWithData("createTxtFileWithData.csv", predictedLabels)
