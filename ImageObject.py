import cv2
import numpy as np
import pyefd

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
        refObject = None

        for obj in ImageData.referenceObjects:

            if(obj.label == self.label):

                ifExists = True
                refObject = obj
                return (ifExists, refObject)

        ImageData.referenceObjects.append(self.imageContour)
        return ifExists, refObject


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
        ifRefObjectExists, refObject = self.AddReferenceObject()

        if(ifRefObjectExists):

            for i in range(len(self.fftResult)):

                self.fftResult[i] = np.exp(1j * i)


    def ComputeFourierDescriptors(self):

        newImage, contours, hierarchy = cv2.findContours(
            self.processedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through all contours found and store each contour's
        # elliptical Fourier descriptor's coefficients.
        coeffs = []
        for cnt in contours:
            # Find the coefficients of all contours
            coeffs.append(pyefd.elliptic_fourier_descriptors(
                np.squeeze(cnt), order=10, normalize=True))

        #coeffs = pyefd.elliptic_fourier_descriptors(self.imageContour, order=10, normalize=True)
        result = np.array(coeffs).flatten()[3:]

        return result