from mnist import MNIST
import os

def LoadNumbersImages():

    numbersImagesDirectory = "Images\\NumberImages"

    for filename in os.listdir(numbersImagesDirectory):

        if("." in filename):

            oldFileName = os.path.join(numbersImagesDirectory, filename)
            newFileName = oldFileName.replace(".", "-")

            os.rename(oldFileName, newFileName)


    mndata = MNIST(numbersImagesDirectory)
    trainImages, trainLabels = mndata.load_training()
    testImages, testLabels = mndata.load_testing()

    #Wyswietla 10 element zbioru
    #print(mndata.display(trainImages[10]))

    return (trainImages, trainLabels, testImages, testLabels)


def LoadOtherImages():

    imagesDirectory = "Images\\OtherImages"
    trainLabels = []
    trainFilePaths = []
    testLabels = []
    testFilePaths = []

    for directoryName in os.listdir(imagesDirectory):

        subDirectory = os.path.join(imagesDirectory, directoryName)
        if("train" in directoryName):

            for trainSubdirectory in os.listdir(subDirectory):

                subDirectory2 = os.path.join(subDirectory, trainSubdirectory)
                trainLabel = trainSubdirectory

                for trainObject in os.listdir(subDirectory2):

                    fullFilePath = os.path.join(subDirectory2, trainObject)
                    trainLabels.append(trainLabel)
                    trainFilePaths.append(fullFilePath)

        elif("test" in directoryName):

            for testObject in os.listdir(subDirectory):

                testLabel = testObject.split("_")[0]
                testLabels.append(testLabel)
                fullFilePath = os.path.join(subDirectory, testObject)
                testFilePaths.append(fullFilePath)


    return (trainFilePaths, trainLabels, testFilePaths, testLabels)


