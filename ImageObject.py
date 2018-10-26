import cv2
import numpy as np
import pyefd

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

        self.imageDescriptors = []


    def ReadImage(self):

        self.image = cv2.imread(self.imagePath)
        self.processedImage = self.image


    def ComputeHuMoments(self):

        self.imageFeatures = cv2.HuMoments(cv2.moments(self.processedImage)).flatten()


    def ComputeCenterOfMass(self):

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
        for y in range(self.imageContour.shape[0]):
            for x in range(self.imageContour.shape[1]):
                if (self.imageContour[y][x] != 0):

                    distance = np.sqrt((y-self.centerOfMass[0])**2 + (x-self.centerOfMass[1])**2)
                    self.rFunction.append(distance)


    def DistanceFFT(self):

        fftResult = np.abs(np.fft.fft(np.array(self.rFunction)))
        self.imageFeatures = fftResult


    def ComputeFourierDescriptors(self, amountOfDescriptors = 10):

        newImage, contours, hierarchy = cv2.findContours(
            self.processedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through all contours found and store each contour's
        # elliptical Fourier descriptor's coefficients.
        coeffs = []
        for cnt in contours:
            # Find the coefficients of all contours
            try:
                coeffs.append(pyefd.elliptic_fourier_descriptors(
                    np.squeeze(cnt), order=10, normalize=True))
            except:
                continue

        self.imageDescriptors = np.array(coeffs).flatten()[3 : 4 + amountOfDescriptors]
        self.imageFeatures = self.imageDescriptors
