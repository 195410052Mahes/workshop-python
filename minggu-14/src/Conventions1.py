from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)
# SVC() (Output)

list(clf.predict(iris.data[:3]))
# [0, 0, 0] (Output)

clf.fit(iris.data, iris.target_names[iris.target])
# SVC() (Output)

list(clf.predict(iris.data[:3]))
# ['setosa', 'setosa', 'setosa'] (Output)