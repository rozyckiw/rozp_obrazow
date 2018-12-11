import cv2
import numpy as np
import os

import sys
from matplotlib import pyplot as plt


def generateFFTimages(directory, label, outputDir):
    extension = ".bmp"
    for filename in os.listdir(directory):
        if filename.startswith(label) and filename.endswith(extension):
            img = cv2.imread(directory+"\\"+filename, 0)
            f = np.fft.fft2(img)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = 20 * np.log(np.abs(fshift))
            fftImageName = filename[:(len(filename) - len(extension))] + "_fftSpectrum" + extension
            cv2.imwrite(outputDir+"\\"+fftImageName, magnitude_spectrum)

def main(args):
    generateFFTimages(args[0], args[1], args[2])

if __name__ == "__main__":
    main(sys.argv[1:])