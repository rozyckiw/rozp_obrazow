import cv2
import numpy as np


def ReadBlackAndWhite(imageObject):

    imageObject.processedImage = cv2.cvtColor(imageObject.processedImage, cv2.COLOR_BGR2GRAY)


def Threshold(imageObject):

    ret, thresholded = cv2.threshold(imageObject.processedImage, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    imageObject.processedImage = thresholded


def Blur(imageObject):

    kernel = np.ones((4,4),np.float32)/25
    imageObject.processedImage = cv2.filter2D(imageObject.processedImage, -1, kernel)


def Sharpen(imageObject):

    kernel_sharpening = np.array([[-1,-1,-1],
                                  [-1, 9,-1],
                                  [-1,-1,-1]])

    imageObject.processedImage = cv2.filter2D(imageObject.processedImage, -1, kernel_sharpening)


def Erosion(imageObject):

    kernel = np.ones((3,3), np.uint8)
    imageObject.processedImage = cv2.erode(imageObject.processedImage, kernel, iterations=2)


def Dilatation(imageObject):

    kernel = np.ones((4,4), np.uint8)
    imageObject.processedImage = cv2.dilate(imageObject.processedImage, kernel, iterations=2)


def Contour(imageObject):

    newImage, contours, hierarchy = cv2.findContours(imageObject.processedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    imageObject.processedImage = cv2.fillPoly(imageObject.processedImage, pts =contours, color=(255,255,255))
    #return cv2.Canny(imageArray, 0, 255)


