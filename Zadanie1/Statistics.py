from pandas_ml import ConfusionMatrix
import ClassificationDataReader as cdr
import matplotlib.pyplot as plt

trueLabels = cdr.readFileToArray("testLabelsMnist.csv")
predictedLabels = cdr.readFileToArray("predictedLabels.csv")
confusion_matrix = ConfusionMatrix(trueLabels, predictedLabels)
confusion_matrix.plot(normalized=True)
confusion_matrix.print_stats()
plt.show()
