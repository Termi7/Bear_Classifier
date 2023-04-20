import os
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from PIL import Image


def preprocess_image(img, model_path='my_model.h5', target_size=(128, 128)):
    # load the model
    model = load_model(model_path)

    # Resize the image to match the input size of the model
    img = img.resize(target_size)

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

    return predicted_class_name


#open the image and convert to Image object
img_path = 'grizzly.jpg'
# img_path = 'polar_bearTest.jpg'
img = Image.open(img_path)

# call preprocess_image() with the Image object as an argument
predicted_class_name = preprocess_image(img)

# print the predicted class name
print('Predicted class:', predicted_class_name)
