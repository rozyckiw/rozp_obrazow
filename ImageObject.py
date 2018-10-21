import cv2

class ImageData:

    def __init__(self, label, image = None, imagePath = None):

        self.label = label
        self.processedImage = None

        if(image):

            self.image = image
            self.processedImage = self.image
        elif(imagePath):

            self.imagePath = imagePath


    def ReadImage(self):

        self.image = cv2.imread(self.imagePath)
        self.processedImage = self.image