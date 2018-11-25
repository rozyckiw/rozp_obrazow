import numpy as np

class TextureFeatures:

    def __init__(self, imageHeight, imageWidth, kernelSize, featureVectors, fileName):

        self.imageSize = (imageHeight, imageWidth)
        self.kernelSize = kernelSize
        self.imageFeatures = featureVectors
        self.fileName = fileName


    def CreateTexture(self, predictions, radiusSize):

        dict = {"linen": 224, "salt": 160, "straw": 96, "wood": 32}
        textureArray = np.zeros(self.imageSize, dtype=np.int32)

        indexY = 0
        # stepYSize = self.kernelSize
        index = 0

        while(indexY < textureArray.shape[0]):

            # if(indexY + stepYSize > textureArray.shape[0]):
            #     stepYSize = textureArray.shape[0] - indexY

            indexX = 0
            # stepXSize = self.kernelSize

            while(indexX < textureArray.shape[1]):

                # if(indexX + stepXSize > textureArray.shape[1]):
                #     stepXSize = textureArray.shape[1] - indexX

                textureArray[indexY:indexY+radiusSize, indexX:indexX+radiusSize] = dict[predictions[index]]

                indexX += radiusSize
                index += 1

            indexY += radiusSize

        self.textureArray = textureArray

