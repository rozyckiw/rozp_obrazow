import cv2
import numpy as np


def ReadBlackAndWhite(imageObject):

    imageObject.processedImage = cv2.cvtColor(imageObject.processedImage, cv2.COLOR_BGR2GRAY)
    imageObject.image = imageObject.processedImage


def Threshold(imageObject):

    ret, thresholded = cv2.threshold(imageObject.processedImage, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    imageObject.processedImage = thresholded


def Bitwise(imageObject):

    imageObject.processedImage = cv2.bitwise_and(imageObject.image, imageObject.processedImage, None)
    ret, thresholded = cv2.threshold(imageObject.processedImage, 0, 255, cv2.THRESH_OTSU)
    imageObject.processedImage = thresholded


def Blur(imageObject):

    #kernel = np.ones((6,6),np.float32)/25
    imageObject.processedImage = cv2.GaussianBlur(imageObject.processedImage, (15,15),  0)


def Sharpen(imageObject):

    kernel_sharpening = np.array([[-1,-1,-1],
                                  [-1, 9,-1],
                                  [-1,-1,-1]])

    imageObject.processedImage = cv2.filter2D(imageObject.processedImage, -1, kernel_sharpening)


def Erosion(imageObject):

    kernel = np.ones((4,4), np.uint8)
    imageObject.processedImage = cv2.erode(imageObject.processedImage, kernel, iterations=1)


def Dilatation(imageObject):

    kernel = np.ones((4,4), np.uint8)
    imageObject.processedImage = cv2.dilate(imageObject.processedImage, kernel, iterations=1)


def Contour(imageObject):

    #newImage, cnts, hierarchy = cv2.findContours(imageObject.processedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #imageObject.processedImage = cv2.fillPoly(imageObject.processedImage, pts =cnts, color=(255,255,255))
    imageObject.imageContour = cv2.Canny(imageObject.processedImage, 0, 255)


def DrawCenterOfMass(imageObject):

    imageObject.imageContour = cv2.circle(imageObject.imageContour, imageObject.centerOfMass, 7, (255, 0, 0), -1)
