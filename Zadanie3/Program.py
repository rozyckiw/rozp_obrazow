import sys
import os
import cv2
import numpy as np
from ImageDislayer import ImageDisplayer as ImDis


IF_DISPLAY_IMAGES = True

def main(args):

    orgImages = LoadImages()
    thresholded = ImagePreprocess(orgImages)
    cannyImages = GetGradientImages(thresholded)

    if(IF_DISPLAY_IMAGES):

        imDisplayer = ImDis(6)
        imDisplayer.DisplayImagesAnimation(cannyImages)


def GetGradientImages(images):

    cannyImages = {}

    for key in images.keys():

        # image = cv2.cvtColor(images[key], cv2.COLOR_BGR2GRAY)
        cannyImages[key] = cv2.Canny(images[key], 0, 255)

    return cannyImages


def ImagePreprocess(images):

    preProceed = {}
    kernel = np.ones((3, 3), np.uint8)

    for key in images.keys():

        image = cv2.cvtColor(images[key], cv2.COLOR_BGR2GRAY)
        # image = cv2.GaussianBlur(image, (5, 5),  0)
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        # image = cv2.dilate(image, kernel, iterations=1)
        # image = cv2.erode(image, kernel, iterations=1)
        # image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        preProceed[key] = image

    return preProceed


def LoadImages():

    imagesDirectory = "Images"
    images = {}

    for imageName in os.listdir(imagesDirectory):

        imDirectory = os.path.join(imagesDirectory, imageName)
        images[imageName] = cv2.imread(imDirectory)

    return images


if __name__ == "__main__":
    main(sys.argv[1:])