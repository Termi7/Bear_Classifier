# Preprocess the image

import os
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from PIL import Image


#load the model
model = load_model('my_model.h5')

img_path = 'polar_bearTest.jpg'
img = Image.open(img_path)


img = img.resize((150, 150))  # Resize to match training data
img = np.asarray(img) / 255.0  # Normalize to match training data

# Add a batch dimension to the image
img = np.expand_dims(img, axis=0)

# Make predictions on the image
predictions = model.predict(img)

# Get the predicted class label
predicted_class_idx = np.argmax(predictions)
data_dir = os.path.join(os.getcwd(), 'data')
class_names = os.listdir(data_dir)
predicted_class = class_names[predicted_class_idx]

print('Predicted class:', predicted_class)