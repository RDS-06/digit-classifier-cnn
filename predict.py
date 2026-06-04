import tensorflow as tf
from tensorflow.keras.datasets import mnist
import numpy as np

model = tf.keras.models.load_model("model.keras")

(_, _), (x_test, y_test) = mnist.load_data()

image = x_test[0] / 255.0
image = image.reshape(1,28,28,1)

prediction = model.predict(image)

print("Predicted:", np.argmax(prediction))
print("Actual:", y_test[0])

import matplotlib.pyplot as plt

plt.imshow(x_test[0], cmap='gray')
plt.title(f"Predicted: {np.argmax(prediction)}")
plt.show()