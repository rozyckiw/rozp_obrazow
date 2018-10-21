from mnist import MNIST
import os
import ImageObject as ImObj

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

    trainImageObjects = []
    testImageObjects = []

    for image, label in zip(trainImages, trainLabels):
        trainImageObjects.append(ImObj.ImageData(label, image=image))

    for image, label in zip(testImages, testLabels):
        testImageObjects.append(ImObj.ImageData(label, image=image))


    #Wyswietla 10 element zbioru
    #print(mndata.display(trainImages[10]))

    return (trainImageObjects, testImageObjects)


def LoadOtherImages():

    imagesDirectory = "Images\\OtherImages"
    trainImages = []
    testImages = []

    for directoryName in os.listdir(imagesDirectory):

        subDirectory = os.path.join(imagesDirectory, directoryName)
        if("train" in directoryName):

            for trainSubdirectory in os.listdir(subDirectory):

                subDirectory2 = os.path.join(subDirectory, trainSubdirectory)
                trainLabel = trainSubdirectory

                for trainObject in os.listdir(subDirectory2):

                    fullFilePath = os.path.join(subDirectory2, trainObject)
                    trainImages.append(ImObj.ImageData(trainLabel, imagePath=fullFilePath))

        elif("test" in directoryName):

            for testObject in os.listdir(subDirectory):

                testLabel = testObject.split("_")[0]
                fullFilePath = os.path.join(subDirectory, testObject)
                testImages.append(ImObj.ImageData(testLabel, imagePath=fullFilePath))


    return (trainImages, testImages)
