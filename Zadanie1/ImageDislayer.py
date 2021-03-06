import matplotlib.pyplot as plt
import numpy as np


class ImageDisplayer:

    def __init__(self, howManyImagesPerPage):

        self.imagesPerPage = howManyImagesPerPage
        self.actualFirstImage = 0
        self.imagePlot = None
        self.allImages = None
        self.allLabels = None


    def DisplayNumberImage(self,  imageArray):

        if (type(imageArray) != np.array):
            imageArray = np.array(imageArray)

        if (imageArray.ndim == 1):
            imageArray = np.reshape(imageArray, (-1, int(np.sqrt(len(imageArray)))))

        plt.figure(0)
        plt.matshow(imageArray)
        plt.show()


    def DisplayNumberImagesAnimation(self, imageObjects):

        self.allImages = [imgObj.processedImage for imgObj in imageObjects]
        self.allLabels = [imgObj.label for imgObj in imageObjects]

        imagesToDisplay = self.allImages[self.actualFirstImage : self.actualFirstImage + self.imagesPerPage]
        labelsToDisplay = [imageObjects[i].label for i in
                           range(self.actualFirstImage, self.actualFirstImage + self.imagesPerPage)]
        self.actualFirstImage += self.imagesPerPage
        self.ImagesAnimation(imagesToDisplay, labelsToDisplay)


    def DisplayOtherImagesAnimation(self, imageObjects):

        self.allImages = [obj.processedImage for obj in imageObjects]
        self.allLabels = [obj.label for obj in imageObjects]

        imagesToDisplay = self.allImages[self.actualFirstImage : self.actualFirstImage + self.imagesPerPage]
        labelsToDisplay = [imageObjects[i].label for i in
                           range(self.actualFirstImage, self.actualFirstImage + self.imagesPerPage)]
        self.actualFirstImage += self.imagesPerPage
        self.ImagesAnimation(imagesToDisplay, labelsToDisplay)


    def keyPressed(self, event):

        if (event.key == ' '):
            self.actualFirstImage += self.imagesPerPage
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

        for i in range(self.imagePlot.shape[0]):
            for j in range(self.imagePlot.shape[1]):

                imageArray = images[imageIndex]

                if (type(imageArray) != np.array):
                    imageArray = np.array(imageArray)

                if (imageArray.ndim == 1):
                    imageArray = np.reshape(imageArray, (-1, int(np.sqrt(len(imageArray)))))

                self.imagePlot[i, j].matshow(imageArray, cmap='gray')
                self.imagePlot[i, j].set_title(labels[imageIndex])
                imageIndex += 1

        plt.show()
