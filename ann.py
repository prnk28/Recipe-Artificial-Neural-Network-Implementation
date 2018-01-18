# Artificial Neural Network

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_json('training.json', lines = True)

X = dataset["cuisine"].values
y = dataset["ingredients"].values

df2 = pd.DataFrame(y)
df3 = df2[0].apply(pd.Series)

result = pd.concat([dataset, df3], axis=1)
result = result.drop('ingredients', axis=1)
result = result.fillna(0)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X = labelencoder_X_1.fit_transform(X)

for column in result.columns:
    if result[column].dtype == type(object):
        le = LabelEncoder()
        result[column] = le.fit_transform(result[column])

X = result["cuisine"].values
y = result.iloc[:, 3:42].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1667, random_state = 0)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 39, kernel_initializer = 'uniform', activation = 'relu', input_dim = 1))

# Adding the second hidden layer
classifier.add(Dense(units = 39, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 39, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 25)

# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
#y_pred = classifier.predict(X_test)
#y_pred = (y_pred > 0.5)
#
## Making the Confusion Matrix
#from sklearn.metrics import confusion_matrix
#cm = confusion_matrix(y_test, y_pred)
