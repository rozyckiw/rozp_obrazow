import sys
import os
import cv2
import numpy as np
from ImageDislayer import ImageDisplayer as ImDis
from CirclePositionsDetector import DetectCirlesPositions as DCP
from Features import HowManyGrapesWithMath


IF_DISPLAY_IMAGES = True

def main(args):

    templateImage, orgImages = LoadImages()
    templateImage = CustomThreshold(templateImage, 3)
    proceedImages = ImagePreprocess(orgImages)
    howManyGrapes = HowManyGrapesWithMath(proceedImages, templateImage)

    # cannyImages = GetGradientImages(proceedImage)
    # signedCirclesImages = DCP(proceedImages)

    if(IF_DISPLAY_IMAGES):

        imDisplayer = ImDis(6)
        imDisplayer.DisplayImagesAnimation(proceedImages, howManyGrapes)


def GetGradientImages(images):

    cannyImages = {}

    for key in images.keys():

        # image = cv2.cvtColor(images[key], cv2.COLOR_BGR2GRAY)
        cannyImages[key] = cv2.Canny(images[key], 50, 255)
        # cnts = cv2.findContours(cannyImages[key].copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # print("{0}: {1}".format(key, len(cnts[0])))

    return cannyImages


def ImagePreprocess(images):

    preProceed = {}
    kernel = np.ones((3, 3), np.uint8)
    kernel2 = np.ones((2, 2), np.uint8)
    kernel_sharpening = np.array([[-1,-1,-1],
                                  [-1, 9,-1],
                                  [-1,-1,-1]])

    for key in images.keys():


        image = CustomThreshold(images[key], 2)
        # image = cv2.cvtColor(images[key], cv2.COLOR_BGR2GRAY)

        # clahe = cv2.createCLAHE(clipLimit=0.2, tileGridSize=(8, 8))
        # image = clahe.apply(image)
        # image = cv2.bilateralFilter(image, 21, 17, 17)
        # image = cv2.medianBlur(image, 3)


        # applying the sharpening kernel to the input image & displaying it.
        # image = cv2.filter2D(image, -1, kernel_sharpening)
        # ret, image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)
        # image = cv2.erode(image, kernel2, iterations=2)

        # image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        # image = cv2.erode(image, kernel2, iterations=2)
        # image = cv2.dilate(image, kernel2, iterations=2)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        # image = cv2.erode(image, kernel2, iterations=2)

        preProceed[key] = image

    return preProceed


def CustomThreshold(image, kernelSize=3):

    def ComputeAverage(imageRegion):

        res = []

        for i in range(3):

            res.append(imageRegion[:,:,i].mean())

        return res


    result = np.zeros((len(image), len(image[0])), dtype=np.float32)
    for i in range(0, len(image), kernelSize):

        iLimit = i + kernelSize if i + kernelSize < len(image) else len(image)
        for j in range(0, len(image[0]), kernelSize):

            jLimit = j + kernelSize if j + kernelSize < len(image[0]) else len(image[0])
            imageRegion = image[i:iLimit, j:jLimit, :]
            regionMean = ComputeAverage(np.array(imageRegion))

            if(np.array(regionMean).mean() < 90): result[i:iLimit, j:jLimit] = 100
            elif(np.array(regionMean).mean() < 200): result[i:iLimit, j:jLimit] = 0
            else: result[i:iLimit, j:jLimit] = 255

            # if(np.array(regionMean).mean() < 200): result[i:iLimit, j:jLimit] = 0
            # else: result[i:iLimit, j:jLimit] = 255

    return result


def HistogramEqualization(image):

    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')


def LoadImages():

    imagesDirectory = "Images"
    images = {}

    for imageName in os.listdir(imagesDirectory):

        imDirectory = os.path.join(imagesDirectory, imageName)

        if ("template" in imageName): template = cv2.imread(imDirectory)
        else: images[imageName] = cv2.imread(imDirectory)

    return template, images


if __name__ == "__main__":
    main(sys.argv[1:])