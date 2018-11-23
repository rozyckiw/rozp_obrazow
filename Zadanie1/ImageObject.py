import cv2
import numpy as np
import pyefd
import ProgramParameters as PP
from skimage.feature import local_binary_pattern
from scipy.misc import imresize


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


    def ComputeImagePartsFeatures(self, radiusSize, featureExtactionMethod):

        indexY = 0
        self.imageFeatures = []
        # stepYSize = radiusSize

        while(indexY < self.processedImage.shape[0]):

            startY = indexY - radiusSize
            finishY = indexY + radiusSize

            if(startY < 0):
                startY = 0

            if(finishY > self.processedImage.shape[0]):
                finishY = self.processedImage.shape[0]

            indexX = 0
            # stepXSize = radiusSize

            while(indexX < self.processedImage.shape[1]):

                startX = indexX - radiusSize
                finishX = indexX + radiusSize

                if(startX < 0):
                    startX = 0

                if(finishX > self.processedImage.shape[1]):
                    finishX = self.processedImage.shape[1]

                im = self.processedImage[startY:finishY,startX:finishX]

                if(featureExtactionMethod == PP.OtherImagesFeaturesType.HuMoments):

                    self.imageFeatures.append(cv2.HuMoments(cv2.moments(im)))

                elif(featureExtactionMethod == PP.OtherImagesFeaturesType.ContourFourierDescriptors):

                    self.imageFeatures.append(self.ComputeFourierDescriptors(10, im))

                elif(featureExtactionMethod == PP.OtherImagesFeaturesType.PowerSpectrum):

                    self.imageFeatures.append(self.LBP(5, im))


                indexX += 1
            indexY += 1


    def GetPowerSpectrum(self, im = None):

        if(not im is None):

            return np.abs(np.fft.fft2(im))**2

        else:
            self.imageFeatures = np.abs(np.fft.fft2(self.processedImage))**2


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


    def kullback_leibler_divergence(self, p, q):

        p = np.asarray(p)
        q = np.asarray(q)
        filt = np.logical_and(p != 0, q != 0)
        return np.sum(p[filt] * np.log2(p[filt] / q[filt]))


    def LBP(self, size, image=None):

        radius = size
        n_points = 8 * radius
        METHOD = 'uniform'

        if(not image is None):

            image = imresize(image, (64, 64))
            lbp = local_binary_pattern(image, n_points, radius, METHOD)

        else: lbp = local_binary_pattern(self.processedImage, n_points, radius, METHOD)

        n_bins = int(lbp.max() + 1)
        ref_hist, _ = np.histogram(lbp, density=True, bins=n_bins, range=(0, n_bins))

        if(not image is None): return ref_hist
        else: self.imageFeatures = ref_hist



    def DistanceFFT(self, valuesAmount):

        fftResult = np.fft.fft(np.array(self.rFunction))
        self.imageFeatures = np.abs(fftResult)

        if(valuesAmount > 0):
            self.InterpolateArray(valuesAmount)


    def InterpolateArray(self, valuesAmount):

        indexesTakenIntoAccount = np.linspace(0, len(self.imageFeatures), valuesAmount, dtype=int)
        newFeatures = []

        for i in range(valuesAmount - 1):

            value = np.mean(self.imageFeatures[indexesTakenIntoAccount[i]:indexesTakenIntoAccount[i+1]])
            newFeatures.append(value)

        self.imageFeatures = newFeatures


    def ComputeFourierDescriptors(self, amountOfDescriptors = 10, imageArray = None):

        if(imageArray is None):

            newImage, contours, hierarchy = cv2.findContours(
                self.processedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        else:

            newImage, contours, hierarchy = cv2.findContours(
                imageArray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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

        self.imageDescriptors = np.array(coeffs).flatten()#[3 : 4 + amountOfDescriptors]

        if(imageArray is None):

            self.imageFeatures = self.imageDescriptors

        else:

            return self.imageDescriptors
