from sklearn import svm
X = [[170, 70, 10], [180, 80, 12], [170, 65, 8], [160, 55, 7]]
Y = [0, 0, 1, 1]
clf = svm.SVC()
clf.fit(X, Y)
p = clf.predict([[161, 59, 8]])
print(p)


