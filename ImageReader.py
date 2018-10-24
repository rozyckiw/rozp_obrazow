from mnist import MNIST
import os
import csv
import ImageObject as ImObj


def saveMnistDataToTxtFile(numbersImagesDirectory):
    for filename in os.listdir(numbersImagesDirectory):

        if ("." in filename):
            oldFileName = os.path.join(numbersImagesDirectory, filename)
            newFileName = oldFileName.replace(".", "-")

            os.rename(oldFileName, newFileName)

    mndata = MNIST(numbersImagesDirectory)
    trainImages, trainLabels = mndata.load_training()
    testImages, testLabels = mndata.load_testing()

    createTxtFileWithData('trainDataMnist.csv', trainImages)
    createTxtFileWithData('testDataMnist.csv', testImages)
    createTxtFileWithData('trainLabelsMnist.csv', trainLabels)
    createTxtFileWithData('testLabelsMnist.csv', testLabels)


def createTxtFileWithData(fileName, data):
    with open(fileName, mode='wb') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if (isinstance(data[0], list)):
            for lineOfData in data:
                data_writer.writerow(lineOfData)
        else:
            for lineOfData in data:
                data_writer.writerow([lineOfData])


def LoadNumbersImages():
    numbersImagesDirectory = "Images\\NumberImages"

    for filename in os.listdir(numbersImagesDirectory):

        if ("." in filename):
            oldFileName = os.path.join(numbersImagesDirectory, filename)
            newFileName = oldFileName.replace(".", "-")

            os.rename(oldFileName, newFileName)

    mndata = MNIST(numbersImagesDirectory)
    trainImages, trainLabels = mndata.load_training()
    testImages, testLabels = mndata.load_testing()

    trainImageObjects = []
    testImageObjects = []

    for image, label in zip(trainImages, trainLabels):
        trainImageObjects.append(ImObj.ImageData(label, image=image))
        # ImObj.ImageData.image

    for image, label in zip(testImages, testLabels):
        testImageObjects.append(ImObj.ImageData(label, image=image))

    # Wyswietla 10 element zbioru
    # print(mndata.display(trainImages[10]))

    return (trainImageObjects, testImageObjects)


def LoadOtherImages():
    imagesDirectory = "Images\\OtherImages"
    trainImages = []
    testImages = []

    for directoryName in os.listdir(imagesDirectory):

        subDirectory = os.path.join(imagesDirectory, directoryName)
        if ("train" in directoryName):

            for trainSubdirectory in os.listdir(subDirectory):

                subDirectory2 = os.path.join(subDirectory, trainSubdirectory)
                trainLabel = trainSubdirectory

                for trainObject in os.listdir(subDirectory2):
                    fullFilePath = os.path.join(subDirectory2, trainObject)
                    trainImages.append(ImObj.ImageData(trainLabel, imagePath=fullFilePath))

        elif ("test" in directoryName):

            for testObject in os.listdir(subDirectory):
                testLabel = testObject.split("_")[0]
                fullFilePath = os.path.join(subDirectory, testObject)
                testImages.append(ImObj.ImageData(testLabel, imagePath=fullFilePath))

    return (trainImages, testImages)
