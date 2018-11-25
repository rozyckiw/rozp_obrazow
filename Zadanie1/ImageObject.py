import cv2
import numpy as np
import pyefd
import ProgramParameters as PP
from skimage.feature import local_binary_pattern
from scipy.misc import imresize
import MyMath as MM
from skimage.feature import greycoprops


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


    def ComputeHuMoments(self, image=None):

        analyzeImage = self.processedImage
        if(not image is None): analyzeImage = image

        if(not image is None): return cv2.HuMoments(cv2.moments(analyzeImage)).flatten()

        self.imageFeatures = cv2.HuMoments(cv2.moments(analyzeImage)).flatten()


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

                im = self.processedImage[indexY:finishY, indexX:finishX]

                if(featureExtactionMethod == PP.OtherImagesFeaturesType.HuMoments):

                    self.imageFeatures.append(cv2.HuMoments(cv2.moments(im)))

                elif(featureExtactionMethod == PP.OtherImagesFeaturesType.ContourFourierDescriptors):

                    self.imageFeatures.append(self.ComputeFourierDescriptors(10, im))

                # elif(featureExtactionMethod == PP.OtherImagesFeaturesType.PowerSpectrum):
                #
                #     self.imageFeatures.append(self.LBP(5, im))

                elif(featureExtactionMethod == PP.OtherImagesFeaturesType.LBP):

                    self.imageFeatures.append(self.LBP(radiusSize, im))

                elif(featureExtactionMethod == PP.OtherImagesFeaturesType.CustomSpace):

                    self.imageFeatures.append(self.CustomSpaceDescriptors(radiusSize, im))

                indexX += radiusSize
            indexY += radiusSize


    def GetPowerSpectrum(self, im = None):

        if(not im is None):

            return np.abs(np.fft.fft2(im))**2

        else:
            self.imageFeatures = np.abs(np.fft.fft2(self.procesedImage))**2


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


    def CustomSpaceDescriptors(self, radius, image=None):

        analyzeImage = self.processedImage

        if(image is not None): analyzeImage = image

        # histogram = MM.createHistogram(analyzeImage)
        # histogramMean = MM.computeMean(histogram)
        #
        # percentiles = MM.getPerentiles(histogram, [50, 90, 99])
        # histogramPerc50 = percentiles[50]
        # histogramPerc90 = percentiles[90]
        # histogramPerc99 = percentiles[99]
        #
        # histogramMode10 = MM.getMode10(histogram)

        glcms = MM.computeGLCM(analyzeImage, radius * 2, 1)
        sumGlcms = np.array([np.sum(els) for els in glcms])
        glcmVal = np.mean(sumGlcms)

        correlations = []
        for glcm in glcms:

            correlations.append(greycoprops(glcm, 'correlation')[0, 0])

        correlation = float(np.mean(correlations))

        lbp = local_binary_pattern(analyzeImage, 8, radius, "uniform")
        lbpHist = MM.createHistogram(lbp)
        lbpVal = MM.getMode(lbpHist)

        huMoments = self.ComputeHuMoments(analyzeImage)
        # descriptors = [histogramMean, histogramPerc50, histogramPerc90, histogramPerc99, histogramMode10,
        #                correlation, glcmVal, lbpVal]
        descriptors = [correlation, glcmVal, lbpVal]
        descriptors.extend(huMoments)

        descriptors = np.array(descriptors, dtype=np.float64)

        if(not image is None): return descriptors

        self.imageFeatures = descriptors


    def LBP(self, radius, image=None):

        radius = 2
        n_points = 8 * radius
        METHOD = 'uniform'

        if(not image is None):

            #image = imresize(image, (64, 64))
            lbp = local_binary_pattern(image, n_points, radius, METHOD)

        else:
            lbp = local_binary_pattern(self.processedImage, n_points, radius, METHOD)

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
