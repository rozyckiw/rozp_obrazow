import cv2
import numpy as np


def ReadBlackAndWhite(imageObject):

    imageObject.processedImage = cv2.cvtColor(imageObject.image, cv2.COLOR_BGR2GRAY)
    imageObject.image = imageObject.processedImage


def RemoveShadows(imageObject):

    rgb_planes = cv2.split(imageObject.image)
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:

        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    #result = cv2.merge(result_planes)
    imageObject.image = cv2.merge(result_norm_planes)


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

    imageObject.imageContour = cv2.Canny(imageObject.processedImage, 0, 255)
    

def DrawCenterOfMass(imageObject):

    imageObject.imageContour = cv2.circle(imageObject.imageContour, imageObject.centerOfMass, 7, (255, 0, 0), -1)


def ExtractImages(imageObjects):

    for imageObj in imageObjects:

        imageObj.ReadImage()
        #RemoveShadows(imageObj)
        ReadBlackAndWhite(imageObj)
        Blur(imageObj)
        Threshold(imageObj)
        Sharpen(imageObj)
        #Bitwise(imageObj)

        if ("spanner" in imageObj.imagePath):
            Erosion(imageObj)
            Dilatation(imageObj)

        Contour(imageObj)
