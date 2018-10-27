import os
import ProgramParameters as PP

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


def SaveFeaturesToFile(imageObjects, labelFilename, dataFilename):

    outputDirectory = "Output"
    dataOutputFile = os.path.join(outputDirectory, dataFilename)
    labelOutputFile = os.path.join(outputDirectory, labelFilename)

    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

    with open(dataOutputFile, 'wb') as df, open(labelOutputFile, 'wb') as lf:

        for imageObj in imageObjects:

            lf.write("{0}\n".format(imageObj.label))
            line = ""

            for feature in imageObj.imageFeatures:
                line += "{0:.5} ".format(feature)

            line += "\n"
            df.write(line)

