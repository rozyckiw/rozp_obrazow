import ImageReader as ImRead
import ImageDislayer as ImDisp


trainImages, testImages = ImRead.LoadOtherImages()
#ImDisp.DisplayNumberImage(trainImages[10])

imDisp = ImDisp.ImageDisplayer(6)
imDisp.DisplayOtherImagesAnimation(trainImages)

#imDisp.DisplayNumberImagesAnimation(trainImages)

#print(trainLabels[10])

#trainFilePaths, trainLabels, testFilePaths, testLabels = ImRead.LoadOtherImages()