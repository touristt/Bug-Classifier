from test_data import test_data
from training_data import training_data
from sklearn.neighbors import KNeighborsClassifier

y_train = [pt['T'] for pt in training_data]  #Training targets
X_train = [[pt['l'], pt['w']] for pt in training_data] #Training data with 2 features (length,width)

y_test = [pt['T'] for pt in test_data]
X_test = [[pt['l'], pt['w']] for pt in test_data]


clf = KNeighborsClassifier(n_neighbors = 2)
clf.fit(X_train,y_train)

print(f"Test set predictions : {clf.predict(X_test)}")
print(f"Test set accuracy : {clf.score(X_test,y_test):.2f}")
