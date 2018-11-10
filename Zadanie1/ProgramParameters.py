from enum import Enum


class OtherImagesFeaturesType(str, Enum):

    ContourFourierDescriptors = "cfd"
    DistanceFourierDescriptors = "dfd"
    HuMoments = "hu"


class ImagesToClassify(str, Enum):

    NumberImages = "numbers"
    OtherImages = "other"
    Textures = "textures"
