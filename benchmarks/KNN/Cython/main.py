import random
from raw import KNN

# Generate a large dataset
num_samples = 10000
num_features = 50

X_train = [[random.uniform(0, 100) for _ in range(num_features)] for _ in range(num_samples)]
y_train_classification = [random.randint(0, 1) for _ in range(num_samples)]
y_train_regression = [random.uniform(0, 100) for _ in range(num_samples)]

# Classification Example
knn_classifier = KNN(k=5, mode="classification")
knn_classifier.fit(X_train, y_train_classification)
prediction_classification = knn_classifier.predict([[random.uniform(0, 100) for _ in range(num_features)]])
print("Classification Prediction:", prediction_classification)

# Regression Example
knn_regressor = KNN(k=5, mode="regression")
knn_regressor.fit(X_train, y_train_regression)
prediction_regression = knn_regressor.predict([[random.uniform(0, 100) for _ in range(num_features)]])
print("Regression Prediction:", prediction_regression)
