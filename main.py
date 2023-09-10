import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Dense, Flatten

# Load the data from the MS Access file
data = pd.read_sql_query("SELECT * FROM weather", "weather")

#Split the data into train and test sets
train_data = data[:10]
test_data = data[10:]

#Create the CNN model
model = Sequential()
model.add(Conv1D(filters=32, kernal_size=3, activation="relu", input_shape=(3,)))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(3, activation="softmax"))

# Train the model
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(train_data, train_data["Humidity"], epochs=10)

#Predict the next 10 days data
predictions = model.predict(test_data)

# Print the predictions
print(predictions)