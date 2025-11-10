# Using the `iris` dataset from sklearn
# create a script that receives the values of the 4 columns `sepal_length`, `sepal_width`, `petal_length` and `petal_width` as arguments
# and the k value for the KNN model
# and prints the predicted species using kNN.

import sys
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# prepare the input values
values = np.array([float(arg.replace(",", "")) for arg in sys.argv[1:-1]])
k = int(sys.argv[-1])

# reshape the values to be a 2D array, which is the expected format for the model
values = values.reshape(1, -1)


def train_model():
    X = iris.data
    y = iris.target
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, y)
    return model


def predict_species(model, values):
    prediction = model.predict(values)
    return prediction[0]


if __name__ == "__main__":
    model = train_model()
    prediction = predict_species(model, values)
    print(f"Input values:")
    print(f"  k neighbors: {k}")
    print(f"  sepal_length: {values[0][0]}")
    print(f"  sepal_width: {values[0][1]}")
    print(f"  petal_length: {values[0][2]}")
    print(f"  petal_width: {values[0][3]}")
    print("--------------------")
    print(f"Predicted species: {iris.target_names[prediction]}")
