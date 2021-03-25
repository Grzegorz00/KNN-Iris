import csv
import math

from Iris import Iris


def fill_dictionary(path):
    train_dictionary = {}
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            iris = Iris(row[0:5], row[5])
            train_dictionary.update({iris: 0.0})
    return train_dictionary


class KNN:

    def __init__(self, k, train_path, test_path):
        self.k = k
        self.train_path = train_path
        self.test_path = test_path

        # key - flower   value - algorithm result label
        self.testList = fill_dictionary(test_path)
        # key - flower   value - distance
        self.train_dictionary = fill_dictionary(train_path)


    def test(self):
        iris = Iris([1, 5.1, 3.5, 1.4, 0.2], "Iris-setosa")
        self.count_distance(iris)

    def count_distance(self, iris):
        for train_iris in self.train_dictionary:
            dist = math.sqrt(
                pow(float(iris.x[0]) - float(train_iris.x[0]), 2)
                + pow(float(iris.x[1]) - float(train_iris.x[1]), 2)
                + pow(float(iris.x[2]) - float(train_iris.x[2]), 2)
                + pow(float(iris.x[3]) - float(train_iris.x[3]), 2)
            )
            self.train_dictionary.update({train_iris: dist})
