import matplotlib.pyplot as plt
import numpy as np


class ImageDisplayer:

    def __init__(self, howManyImagesPerPage):

        self.imagesPerPage = howManyImagesPerPage
        self.actualFirstImage = 0
        self.imagePlot = None
        self.allImages = None
        self.allLabels = None


    def DisplayImagesAnimation(self, images):

        self.allImages = [images[key] for key in images.keys()]
        self.allLabels = [key for key in images.keys()]

        imagesToDisplay = self.allImages[self.actualFirstImage : self.actualFirstImage + self.imagesPerPage]
        labelsToDisplay = [self.allLabels[i] for i in
                           range(self.actualFirstImage, self.actualFirstImage + self.imagesPerPage)]
        # self.actualFirstImage += self.imagesPerPage
        self.ImagesAnimation(imagesToDisplay, labelsToDisplay)


    def keyPressed(self, event):

        if (event.key == 'x'):

            if(self.actualFirstImage + self.imagesPerPage <= len(self.allImages)):

                self.actualFirstImage += self.imagesPerPage
                self.UpdatePlot()

        elif (event.key == 'z'):

            if(self.actualFirstImage - self.imagesPerPage >= 0):

                self.actualFirstImage -= self.imagesPerPage
                self.UpdatePlot()


    def ImagesAnimation(self, images, labels):

        yElements = (self.imagesPerPage // 3)
        if (self.imagesPerPage % 3 != 0):
            yElements += 1

        f, self.imagePlot = plt.subplots(yElements, 3)
        f.canvas.mpl_connect('key_press_event', self.keyPressed)
        imageIndex = 0

        for i in range(self.imagePlot.shape[0]):
            for j in range(self.imagePlot.shape[1]):

                imageArray = images[imageIndex]

                if (type(imageArray) != np.array):
                    imageArray = np.array(imageArray)

                if (imageArray.ndim == 1):
                    imageArray = np.reshape(imageArray, (-1, int(np.sqrt(len(imageArray)))))

                self.imagePlot[i, j].matshow(imageArray, cmap='gray')
                self.imagePlot[i, j].set_title(labels[imageIndex])
                self.imagePlot[i, j].axis('off')
                imageIndex += 1

        plt.show()


    def UpdatePlot(self):

        images = self.allImages[self.actualFirstImage:self.actualFirstImage + self.imagesPerPage]
        labels = self.allLabels[self.actualFirstImage:self.actualFirstImage + self.imagesPerPage]
        imageIndex = 0
        cont = True

        for i in range(self.imagePlot.shape[0]):

            if(not cont): break

            for j in range(self.imagePlot.shape[1]):

                if(imageIndex >= len(images)): cont = False
                if(not cont): break

                imageArray = images[imageIndex]

                if (type(imageArray) != np.array):
                    imageArray = np.array(imageArray)

                if (imageArray.ndim == 1):
                    imageArray = np.reshape(imageArray, (-1, int(np.sqrt(len(imageArray)))))

                self.imagePlot[i, j].matshow(imageArray, cmap='gray')
                self.imagePlot[i, j].set_title(labels[imageIndex])
                imageIndex += 1

        plt.show()
