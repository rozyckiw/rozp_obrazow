import sys
import ImageReader as ImRead
import ImageDislayer as ImDisp
import ImageSegmentation as imSeg
import Features
import ProgramParameters as PP


def main(args):

    images = "other"
    featureMethod = "hu"
    ifDisplayImages = True

    imagesToClassify = PP.ImagesToClassify(images)
    featureExtactionMethod = PP.OtherImagesFeaturesType(featureMethod)


    if(imagesToClassify == PP.ImagesToClassify.NumberImages):

        print("Loading number images..")
        trainImages, testImages = ImRead.LoadNumbersImages()

    elif(imagesToClassify == PP.ImagesToClassify.OtherImages):

        print("Loading other images..")
        trainImages, testImages = ImRead.LoadOtherImages()

        print("Processing images..")
        imSeg.ExtractImages(trainImages)
        imSeg.ExtractImages(testImages)

        print("Computing shape descriptors..")
        Features.ComputeFeatures(trainImages, featureExtactionMethod)
        Features.ComputeFeatures(testImages, featureExtactionMethod)

        trainData = "otherImagesTrain.txt"
        trainLabels = "otherImagesLabelsTrain.txt"
        testData = "otherImagesTest.txt"
        testLabels = "otherImagesLabelsTest.txt"

    print("Saving features to file")
    Features.SaveFeaturesToFile(trainImages, trainLabels, trainData)
    Features.SaveFeaturesToFile(testImages, testLabels, testData)

    if(ifDisplayImages):

        imDisp = ImDisp.ImageDisplayer(6)
        imDisp.DisplayOtherImagesAnimation(testImages)


if __name__ == "__main__":
    main(sys.argv[1:])