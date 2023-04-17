# Preprocess the image

import os
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from PIL import Image

#load the model
model = load_model('my_model.h5')

# img_path = 'polar_bearTest.jpg'
img_path = 'test2teddy_bear.jpg'
img = Image.open(img_path)

# Resize the image to match the input size of the model
img = img.resize((128, 128))
# img = img.resize((480, 640))

# Convert the image to a numpy array and normalize its pixel values
image_array = np.array(img) / 255.0

# Reshape the numpy array to have a batch dimension of 1
image_array = image_array.reshape((1,) + image_array.shape)


# Use the model to make a prediction on the image
prediction = model.predict(image_array)

# Get the index of the class with the highest probability
predicted_class_index = np.argmax(prediction)

# Get the name of the predicted class
data_dir = os.path.join(os.getcwd(), 'data')
class_names = os.listdir(data_dir)
predicted_class_name = class_names[predicted_class_index]

# Print out prediction, info and facts about the type of bear.
if predicted_class_name == "teddy":
    print('Predicted class:', predicted_class_name, '\n')
    with open("Bear Facts/TeddyFacts.txt") as file_object:
        for line in file_object:
            l = line.replace("\n", "")
            print(l)
elif predicted_class_name == "polar":
    print('Predicted class:', predicted_class_name, '\n')
    with open("Bear Facts/PolarFacts.txt") as file_object:
        for line in file_object:
            l = line.replace("\n", "")
            print(l)
elif predicted_class_name == "black":
    print('Predicted class:', predicted_class_name, '\n')
    with open("Bear Facts/BlackFacts.txt") as file_object:
        for line in file_object:
            l = line.replace("\n", "")
            print(l)
elif predicted_class_name == "panda":
    print('Predicted class:', predicted_class_name, '\n')
    with open("Bear Facts/PandaFacts.txt") as file_object:
        for line in file_object:
            l = line.replace("\n", "")
            print(l)
elif predicted_class_name == "grizzly":
    print('Predicted class:', predicted_class_name, '\n')
    with open("Bear Facts/GrizzlyFacts.txt") as file_object:
        for line in file_object:
            l = line.replace("\n", "")
            print(l)
else:
    print("NONE")
