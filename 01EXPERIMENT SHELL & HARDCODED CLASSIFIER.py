import random
from sklearn import datasets
iris = datasets.load_iris()

#create a new array that will store the iris data and targets
myArray = []

#Fill myArray with iris data and target.
for i, data in enumerate(iris.data):
    tempTarget = i/50
    tempArray = [data, tempTarget]
    myArray.append(tempArray)

#Trying to randomize iris
random.shuffle(myArray)

#separate training set and test set
trainingSet = myArray[:105]
testSet = myArray[105:]

#
class HardCoded:
    def train(self, trainingSet):
        return 0

    def predict(self, testSet):
        predictions = []
        for i, data in enumerate(testSet):
            predictions.append(0)
        return predictions

    def evauluate(self, predictions, testSet):
        correctCount = 0.0
        totalCount = 0.0
        for i, data in enumerate(testSet):
            totalCount +=1
            if predictions[i] == data[1]:
                correctCount +=1

        percentage = correctCount / totalCount
        return percentage

train = HardCoded()

train.train(trainingSet)
predictions = train.predict(testSet)
percentage =  train.evauluate(predictions, testSet)
finalAnswer = percentage * 100
print("%.2f" % finalAnswer) + "%"





