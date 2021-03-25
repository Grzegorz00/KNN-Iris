from KNN import KNN

k = input("Enter k value: ")
# test_path = input("Enter test-set path name: ")
# train_path = input("Enter train-set path name: ")

test_path = "D:\\Studia\\PJATK\\Sem4\\NAI\\Ćwiczenia\\Lab2\\Projekt\\KNN-Iris\\dane\\test-set.csv"
train_path = "D:\\Studia\\PJATK\\Sem4\\NAI\\Ćwiczenia\\Lab2\\Projekt\\KNN-Iris\\dane\\train-set.csv"

knn = KNN(k, train_path, test_path)
knn.test()





# exit = False
#
# while not exit:
#
#     x = input("Press x to exit")
#     if x == 'x':
#         exit = True
#
# print("End")