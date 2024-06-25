import tensorflow as tf
from tensorflow import keras
import numpy as np

# Create a simple neural network model
model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Dummy data for example
data = np.random.random((1000, 784))
labels = np.random.randint(10, size=(1000,))

# Train the model
model.fit(data, labels, epochs=10)

