import cv2
import numpy as np


def ReadBlackAndWhite(fileName):

    img = cv2.imread(fileName)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def Threshold(imageArray):

    ret, thresholded = cv2.threshold(imageArray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresholded


def Blur(imageArray):

    kernel = np.ones((4,4),np.float32)/25
    return cv2.filter2D(imageArray,-1,kernel)


def Sharpen(imageArray):

    kernel_sharpening = np.array([[-1,-1,-1],
                                  [-1, 9,-1],
                                  [-1,-1,-1]])

    return cv2.filter2D(imageArray, -1, kernel_sharpening)


def Erosion(imageArray):

    kernel = np.ones((3,3), np.uint8)
    return cv2.erode(imageArray, kernel, iterations=2)


def Dilatation(imageArray):

    kernel = np.ones((4,4), np.uint8)
    return cv2.dilate(imageArray, kernel, iterations=2)


def Contour(imageArray):

    newImage, contours, hierarchy = cv2.findContours(imageArray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return cv2.fillPoly(imageArray, pts =contours, color=(255,255,255))
    #return cv2.Canny(imageArray, 0, 255)


