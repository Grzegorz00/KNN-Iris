import csv
import math

from Iris import Iris


def fill_dictionary(path):
    train_dictionary = {}
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            iris = Iris(row[1:5], row[5])
            train_dictionary.update({iris: 0.0})
    return train_dictionary


class KNN:

    def __init__(self, k, train_path, test_path):
        self.k = k
        self.train_path = train_path
        self.test_path = test_path

        # key - flower   value - algorithm result label
        self.test_list = fill_dictionary(test_path)
        # key - flower   value - distance
        self.train_dictionary = fill_dictionary(train_path)
        self.accuracy = 0

    def test_file(self):
        for key, value in self.test_list.items():
            self.count_distance(key)
            self.test_list.update({key: self.find_best_label()})

    def print_output(self):
        print("Test value: -> Trained value:")
        for key, value in self.test_list.items():
            print(str(key.y) + " -> " + str(value))
        print("Accuracy: " + str(self.count_accuracy()))

    def test_element(self, iris):
        self.count_distance(iris)
        print(str(iris.x) + " " + str(self.find_best_label()))

    def count_accuracy(self):
        correct = 0
        for key, value in self.test_list.items():
            correct = correct + 1 if str(key.y) == str(value) else correct

        return str(correct / len(self.test_list))

    def count_distance(self, iris):
        for train_iris in self.train_dictionary:
            dist = math.sqrt(
                pow(float(iris.x[0]) - float(train_iris.x[0]), 2)
                + pow(float(iris.x[1]) - float(train_iris.x[1]), 2)
                + pow(float(iris.x[2]) - float(train_iris.x[2]), 2)
                + pow(float(iris.x[3]) - float(train_iris.x[3]), 2)
            )
            self.train_dictionary.update({train_iris: dist})

    def find_best_label(self):
        self.train_dictionary = {
            k: v for k, v in sorted(self.train_dictionary.items(), key=lambda v: v[1])
        }

        k_elements = []

        for i in range(0, int(self.k)):
            k_elements.append(list(self.train_dictionary.keys())[i])

        return max(set(k_elements), key=k_elements.count)
