import sys
import ImageReader as ImRead
import ImageDislayer as ImDisp
import ImageSegmentation as imSeg
import Features
import ProgramParameters as PP
import OtoczenieKuliste as OK
import KNN

def main(args):

    images = "textures"
    featureMethod = "hu"
    classMethod = "otKul"
    ifDisplayImages = False
    ifClassify = True

    imagesToClassify = PP.ImagesToClassify(images)
    featureExtactionMethod = PP.OtherImagesFeaturesType(featureMethod)
    classificationMethod = PP.ClassificationMethod(classMethod)

    if not ifClassify:

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

            trainData = "OtherImages\\trainData.txt"
            trainLabels = "OtherImages\\trainLabels.txt"
            testData = "OtherImages\\testData.txt"
            testLabels = "OtherImages\\testLabels.txt"

            Features.SaveFeaturesToFile(trainImages, trainLabels, trainData)

        elif(imagesToClassify == PP.ImagesToClassify.Textures):

            print("Loading textures..")
            trainImages, testImages = ImRead.LoadTextures()

            print("Processing images..")
            imSeg.ExtractImages(trainImages, onlyConvertToGreyScale=True)
            imSeg.ExtractImages(testImages, onlyConvertToGreyScale=True)

            print("Computing hu moments..")
            kernelSize = 5
            Features.ComputeFeatures(trainImages, PP.OtherImagesFeaturesType.HuMoments)
            Features.ComputeTexturePartFeatures(testImages, kernelSize)

            trainData = "Textures\\trainData.txt"
            trainLabels = "Textures\\trainLabels.txt"

            print("Saving features to file")
            Features.SaveFeaturesToFile(trainImages, trainLabels, trainData)
            Features.SaveImagePartsFeatures(testImages, kernelSize)


    elif ifClassify:

        print("Classification started!")
        featureFiles = ["test1.txt", "test2.txt", "test3.txt"]
        textureObjects = []

        for featureFile in featureFiles:

            textureObjects.append(Features.ReadFeaturesOfImage(featureFile))

        trainData = "Textures\\trainData.txt"
        trainLabels = "Textures\\trainLabels.txt"
        predictions = []

        if(classificationMethod == PP.ClassificationMethod.OtoczenieKuliste):

            OtKul = OK.OtoczKul(trainData, trainLabels)

            for textureObj in textureObjects:

                predictions.append([])

                for imageFeatures in textureObj.imageFeatures:

                    predictions[-1].append(OtKul.PredictLabel(imageFeatures))

                textureObj.CreateTexture(predictions[-1])
                Features.SaveImage(textureObj)

        elif(classificationMethod == PP.ClassificationMethod.KNN):

            knn = KNN.KNN(trainData, trainLabels, 3)

            for textureObj in textureObjects:

                predictions.append([])

                for imageFeatures in textureObj.imageFeatures:

                    predictions[-1].append(knn.predict(imageFeatures))

                textureObj.CreateTexture(predictions[-1])
                Features.SaveImage(textureObj)


    if(ifDisplayImages):

        imDisp = ImDisp.ImageDisplayer(6)
        imDisp.DisplayOtherImagesAnimation(trainImages)


if __name__ == "__main__":
    main(sys.argv[1:])