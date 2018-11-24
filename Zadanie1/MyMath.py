from skimage.feature import greycomatrix


def createHistogram(image):

    histogram = {}
    for i in image.ravel():
        histogram[i] = histogram.get(i, 0) + 1

    return histogram


def computeMean(dict):

    nominator   = 0.
    denominator = 0.

    for key, val in dict.iteritems():

        denominator += key
        nominator += key * val

    return float(nominator / denominator)


def getPerentiles(dict, percentiles):

    noElements = sum(dict.values())
    result = {}
    actualElements = 0

    for key, val in dict.iteritems():

        if(len(percentiles) == 0): break

        actualElements += val
        percentage = 100 * actualElements / noElements

        for percentile in percentiles:

            if(percentage >= percentile):

                result[percentile] = float(key)
                percentiles.remove(percentile)
                break

    if(len(percentiles) > 0):

        for percentile in percentiles:

            result[percentile] = float(dict.keys()[-1])

    return result


def getMode(histogram):

    maxim = 0
    result = 0

    for key, val in histogram.iteritems():

        if(val > maxim):

            maxim = val
            result = key

    return float(result)


def getMode10(histogram):

    histogramCp = dict(histogram)
    histogramMode = 0
    maxim10 = 0
    keys = list(histogramCp.keys())

    for i in range(1, len(keys)):

        histogramCp[keys[i]] += histogramCp[keys[i-1]]

    for i in range(len(histogramCp) - 0x10):

        if(histogramCp[keys[i + 0x10]] - histogramCp[keys[i]] > maxim10):

            maxim10 = histogramCp[keys[i + 0x10]]-histogramCp[keys[i]]
            histogramMode = i

    return float(histogramMode)


def computeGLCM(image, patchSize, offset):

    glcms = []
    for y in range(0, image.shape[0], patchSize):

        startY = y - patchSize
        finishY = y + patchSize

        if(startY < 0):
            startY = 0

        if(finishY >  image.shape[0]):
            finishY = image.shape[0]

        for x in range(0, image.shape[1], patchSize):

            startX = x - patchSize
            finishX = x + patchSize

            if(startX < 0):
                startX = 0

            if(finishX > image.shape[1]):
                finishX = image.shape[1]

            img = image[startY:finishY, startX:finishX]
            glcms.append(greycomatrix(img, [offset], [0], 256, symmetric=True, normed=True))

    return glcms