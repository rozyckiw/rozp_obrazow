import ImageReader as ImRead
import ImageDislayer as ImDisp


trainImages, trainLabels, testImages, testLabels = ImRead.LoadOtherImages()
#ImDisp.DisplayNumberImage(trainImages[10])

imDisp = ImDisp.ImageDisplayer(6)
imDisp.DisplayOtherImagesAnimation(trainImages, trainLabels)

#ImDisp.DisplayNumberImagesAnimation(trainImages, trainLabels, 6)

#print(trainLabels[10])

#trainFilePaths, trainLabels, testFilePaths, testLabels = ImRead.LoadOtherImages()