from matplotlib import pyplot as plt
from KNN import KNN


class Figure:

    def __init__(self, k_range, train_path, test_path):
        self.k_range = k_range
        self.train_path = train_path
        self.test_path = test_path
        self.scores_list = self.get_scores_list()

    def get_scores_list(self):
        scores_list = []
        for k in self.k_range:
            knn = KNN(k, self.train_path, self.test_path)
            knn.test_file()
            scores_list.append(float(knn.count_accuracy()))
        return scores_list

    def visualise(self):

        plt.plot(self.k_range, self.scores_list)
        plt.xlabel('Value of K')
        plt.ylabel('Testing Accuracy')
        plt.show()
