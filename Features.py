import os


def SaveFeaturesToFile(imageObjects, filename):

    outputDirectory = "Output"
    outputFile = os.path.join(outputDirectory, filename)

    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

    with open(outputFile, 'wb') as f:

        for imageObj in imageObjects:

            line = "{0}:".format(imageObj.label)

            for feature in imageObj.imageDescriptors:
                line += "{0:.5} ".format(feature)

            line += "\n"
            f.write(line)

