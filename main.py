from KNN import KNN
from Iris import Iris
from Figure import Figure

k = input("Enter k value: ")
# test_path = input("Enter test-set path name: ")
# train_path = input("Enter train-set path name: ")
test_path = "D:\\Studia\\PJATK\\Sem4\\NAI\\Ćwiczenia\\Lab2\\Projekt\\KNN-Iris\\dane\\test-set.csv"
train_path = "D:\\Studia\\PJATK\\Sem4\\NAI\\Ćwiczenia\\Lab2\\Projekt\\KNN-Iris\\dane\\train-set.csv"

knn = KNN(k, train_path, test_path)
knn.test_file()
knn.print_output()
figure = Figure(range(1, 25), train_path, test_path)
figure.visualise()

exit_program = False
while not exit_program:
    print("\n\n\nGive vector")
    knn.test_element(Iris([input(), input(), input(), input(), input()], ""))

    x = input("Press x to exit: ")
    if x == 'x':
        exit_program = True

print("End")
