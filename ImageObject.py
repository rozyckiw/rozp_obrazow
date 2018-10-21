import cv2
import numpy as np


class ImageData:

    def __init__(self, label, image = None, imagePath = None):

        self.label = label
        self.processedImage = None
        self.imageContour = None

        if(image):

            self.image = image
            self.processedImage = self.image

        elif(imagePath):

            self.imagePath = imagePath

        #Features
        self.centerOfMass = None


    def ReadImage(self):

        self.image = cv2.imread(self.imagePath)
        self.processedImage = self.image


    def ComputeCenterOfMass(self):

        xSum = 0
        ySum = 0
        allElements = 0

        for x in range(self.processedImage.shape[0]):

            for y in range(self.processedImage.shape[1]):

                if(self.processedImage[x, y] == 255):

                    xSum += x
                    ySum += y
                    allElements += 1

        self.centerOfMass = (xSum / allElements, ySum / allElements)


    def ComputeBasicObjectProperties(self):

        self.circuit = 0
        self.area = 0
        self.centerOfMass = None
        xSum = 0
        ySum = 0

        for indexX, (contourPix, imagePix) in enumerate(zip(self.imageContour, self.processedImage)):

            self.circuit += np.count_nonzero(contourPix)

            for indexY, pixelValue in enumerate(imagePix):

                if (pixelValue != 0):

                    self.area += 1
                    xSum += indexX
                    ySum += indexY

        self.centerOfMass = (xSum / self.area, ySum / self.area)
