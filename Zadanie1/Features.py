import os
import ProgramParameters as PP
import TextureSegmentation as TS
import scipy.misc
import numpy as np
import datetime


def ComputeFeatures(imageObjects, method, interpolateTo = 100):

    for imageObj in imageObjects:

        if(method == PP.OtherImagesFeaturesType.ContourFourierDescriptors):

            imageObj.ComputeFourierDescriptors()

        elif(method == PP.OtherImagesFeaturesType.DistanceFourierDescriptors):

            imageObj.ComputeCenterOfMass()
            imageObj.DetermineDistanceFunction()
            imageObj.DistanceFFT(interpolateTo)

        elif(method == PP.OtherImagesFeaturesType.HuMoments):

            imageObj.ComputeHuMoments()

        elif(method == PP.OtherImagesFeaturesType.PowerSpectrum):

            imageObj.LBP(5)

        elif(method == PP.OtherImagesFeaturesType.CustomSpace):

            imageObj.CustomSpaceDescriptors()


def ComputeTexturePartFeatures(imageObjects, kernelSize, featureExtactionMethod):

    import threading

    threads = []
    for imageObj in imageObjects:

        if(not "label" in imageObj.label):

            threads.append(threading.Thread(target=RunThread, args=(imageObj, kernelSize, featureExtactionMethod)))
            threads[-1].start()

    for i in range(len(threads)):

        threads[i].join()
        #print("{0} Test feature extraction of {1} finished!".format(datetime.datetime.now(), i))


def RunThread(imageObj, kernelSize, featureExtractionMethod):

    print("{0} Computing  features of {1}".format(datetime.datetime.now(), imageObj.label))
    imageObj.ComputeImagePartsFeatures(kernelSize, featureExtractionMethod)


def SaveImage(textureObject):

    outputDir = "Output\\Textures\\"
    fileName = textureObject.fileName.split(".")[0] + ".jpg"
    fileName = outputDir+fileName
    scipy.misc.toimage(textureObject.textureArray, cmin=0, cmax=255).save(fileName)


def ReadFeaturesOfImage(fileName):

    outputDirectory = "Output\\Textures"
    dataInputFile = os.path.join(outputDirectory, fileName)

    if not os.path.isfile(dataInputFile):

        print("File not found!")
        return None

    with open(dataInputFile) as df:

        all_lines = df.readlines()
        imageHeight, imageWidth = (int(val) for val in all_lines[0].split())
        inputVectors = [[float(val) for val in line.split()] for line in all_lines[1:]]

    textureObject = TS.TextureFeatures(imageHeight, imageWidth, 0, inputVectors, fileName)

    return textureObject


def SaveImagePartsFeatures(imageObjects):

    outputDirectory = "Output\\Textures"

    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)


    for imageObj in imageObjects:

        if(not "label" in imageObj.label):

            dataOutputFile = os.path.join(outputDirectory, imageObj.label.split('.')[0]+".txt")

            with open(dataOutputFile, 'wb') as df:

                imageSize = imageObjects[0].image.shape
                df.write("{0} {1}\n".format(imageSize[0], imageSize[1]))
                line = ""

                for features in imageObj.imageFeatures:

                    if(len(features) > 0):

                        for feature in features:

                            if(type(feature) is np.float64):

                                line += "{0} ".format(feature)

                            else:

                                for precFeature in feature.ravel():

                                    line += "{0:.5} ".format(precFeature)

                                # line += "{0} ".format(feature[0])

                        line += "\n"

                df.write(line)


def SaveFeaturesToFile(imageObjects, labelFilename, dataFilename):

    outputDirectory = "Output"
    dataOutputFile = os.path.join(outputDirectory, dataFilename)
    labelOutputFile = os.path.join(outputDirectory, labelFilename)
    subDirectory = dataOutputFile[0:dataOutputFile.rindex('\\')]

    if not os.path.exists(subDirectory):
        os.makedirs(subDirectory)

    with open(dataOutputFile, 'wb') as df, open(labelOutputFile, 'wb') as lf:

        for imageObj in imageObjects:

            lf.write("{0}\n".format(imageObj.label))
            line = ""

            for feature in imageObj.imageFeatures:

                if(not type(feature) is np.ndarray): line += "{0:.5} ".format(feature)
                else:

                    for precFeature in feature:

                        line += "{0:.5} ".format(precFeature)

            line += "\n"
            df.write(line)

