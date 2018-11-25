from enum import Enum


class OtherImagesFeaturesType(str, Enum):

    ContourFourierDescriptors = "cfd"
    DistanceFourierDescriptors = "dfd"
    HuMoments = "hu"
    PowerSpectrum = "ps"
    LBP = "lbp"
    CustomSpace = "cu"


class ImagesToClassify(str, Enum):

    NumberImages = "numbers"
    OtherImages = "other"
    Textures = "textures"


class ClassificationMethod(str, Enum):

    KNN = "knn"
    OtoczenieKuliste = "otKul"
    Percepton = "perc"