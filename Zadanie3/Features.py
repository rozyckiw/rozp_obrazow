import cv2
import math
import numpy as np


def GetHuMoments(image):

    return cv2.HuMoments(cv2.moments(image)).flatten()


def HowManyGrapesWithMath(images, templateImage):

    templatePixelAmount = CountHowManyGrapes(templateImage, True)
    result = {}

    for key in images.keys():

        redPixelsAmount, yellowPixelsAmount = CountHowManyGrapes(images[key])
        result[key] = (int(redPixelsAmount / templatePixelAmount),
                       int(yellowPixelsAmount / templatePixelAmount))

    return result


def CountHowManyGrapes(image, reference=False):

    if(reference):

        return image.size - list(image.flatten()).count(255)

    return list(image.flatten()).count(100), list(image.flatten()).count(0)


def HowManyGrapesInImagesWithHu(images, templateImage):

    result = {}

    for key in images.keys():
        result[key] = HowManyGrapesInOneImage(images[key], templateImage)

    return result


def HowManyGrapesInOneImage(image, templateImage):

    iStep = 1
    jStep = 1
    result = 0
    tempHeight = len(templateImage)
    tempWidth = len(templateImage[0])

    for i in range(0, len(image), iStep):

        iStep = 1
        iLimit = i + iStep + tempHeight if i + iStep + tempHeight < len(image) else len(image)

        for j in range(0, len(image[0]), jStep):

            jStep = 1
            jLimit = j + jStep + tempWidth if j + jStep + tempWidth < len(image[0]) else len(image[0])
            imageRegion = image[i:iLimit, j:jLimit]

            if (IfImageIsSimilarToTemplate(imageRegion, templateImage)):
                image[i:iLimit, j:jLimit] = 50
                result += 1
                iStep = tempHeight
                jStep = tempWidth

    return result


def IfImageIsSimilarToTemplate(image, templateImage):

    def ComputeDistance(point1, point2):

        dist = 0

        for i in range(len(point1)):
            dist += (point2[i] - point1[i]) ** 2

        return math.sqrt(dist)

    templateHuMoments = GetHuMoments(templateImage)
    imageHuMoments = GetHuMoments(image)
    distance = ComputeDistance(imageHuMoments, templateHuMoments)

    if (distance < 0.00001):
        return True
    else:
        return False
