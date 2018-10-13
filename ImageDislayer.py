import matplotlib.pyplot as plt
import numpy as np

def DisplayNumberImage(imageArray):

    if(type(imageArray) != np.array):

        imageArray = np.array(imageArray)

    if(imageArray.ndim == 1):
        imageArray = np.reshape(imageArray, (-1, int(np.sqrt(len(imageArray)))))

    plt.matshow(imageArray)
    plt.show()