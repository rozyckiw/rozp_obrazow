import cv2
import numpy as np


class ImageData:

    referenceObjects = []

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


    def AddReferenceObject(self):

        ifExists = False

        for obj in ImageData.referenceObjects:

            if(obj.label == self.label): ifExists = True

        if not ifExists:
            ImageData.referenceObjects.append(self.imageContour)


    def ReadImage(self):

        self.image = cv2.imread(self.imagePath)
        self.processedImage = self.image


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

        self.centerOfMass = (ySum / self.area, xSum / self.area)


    def DetermineDistanceFunction(self):

        self.rFunction = []
        for x in range(self.imageContour.shape[0]):
            for y in range(self.imageContour.shape[1]):
                if (self.imageContour[x][y] != 0):

                    distance = np.sqrt((x-self.centerOfMass[0])**2 + (y-self.centerOfMass[1])**2)
                    self.rFunction.append(distance)


    def ComputeAndNormalizeFFT(self):

        self.fftResult = np.fft.fft(np.array(self.rFunction))

        for i in range(len(self.fftResult)):

            self.fftResult[i] = np.exp(1j * i)