import ImageReader as ImRead
import ImageDislayer as ImDisp
import ImageSegmentation as imSeg
import Features


trainImages, testImages = ImRead.LoadOtherImages()
#ImRead.saveMnistDataToTxtFile("Images\\NumberImages")
# ImDisp.DisplayNumberImage(trainImages[10])

imSeg.ExtractImages(trainImages)
imSeg.ExtractImages(testImages)

Features.SaveFeaturesToFile(trainImages, "otherImagesTrain.txt")
Features.SaveFeaturesToFile(testImages, "otherImagesTest.txt")

#imDisp = ImDisp.ImageDisplayer(6)
#imDisp.DisplayOtherImagesAnimation(trainImages)