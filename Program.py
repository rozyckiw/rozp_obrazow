import ImageReader as ImRead
import ImageDislayer as ImDisp


trainImages, trainLabels, testImages, testLabels = ImRead.LoadNumbersImages()
#ImDisp.DisplayNumberImage(trainImages[10])

imDisp = ImDisp.ImageDisplayer(6)
imDisp.DisplayNumberImagesAnimation(trainImages, trainLabels)

#ImDisp.DisplayNumberImagesAnimation(trainImages, trainLabels, 6)

#print(trainLabels[10])

#trainFilePaths, trainLabels, testFilePaths, testLabels = ImRead.LoadOtherImages()