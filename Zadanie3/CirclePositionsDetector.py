import cv2
import numpy as np


def DetectCirlesPositions(images):

    signedCirclesImages = {}

    for key in images.keys():

        # image = cv2.cvtColor(images[key], cv2.COLOR_BGR2GRAY)
        signedCirclesImages[key] = MakeHough(images[key])
        # cnts = cv2.findContours(cannyImages[key].copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # print("{0}: {1}".format(key, len(cnts[0])))

    return signedCirclesImages


def MakeHough(image):

    # detect circles in the image
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.3, 100)
    output = image.copy()

    # ensure at least some circles were found
    if circles is not None:

        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:

            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 14)
            output = cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    return output