import os
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.applications import VGG16
from keras.optimizers import Adam
from keras.optimizers import RMSprop
from PIL import Image

data_dir = os.path.join(os.getcwd(), 'data')
class_names = os.listdir(data_dir)
class_names = [class_name for class_name in class_names if not class_name.startswith('.')]  # add this line
num_class = len(class_names)
image_files = [[os.path.join(data_dir, class_name, x)
                for x in os.listdir(os.path.join(data_dir, class_name)) if not x.startswith('.')]  # add this line
               for class_name in class_names]

image_file_list = []
image_label_list = []
for i, class_name in enumerate(class_names):
    image_file_list.extend(image_files[i])
    image_label_list.extend([i] * len(image_files[i]))
num_total = len(image_label_list)

image_width, image_height = Image.open(image_file_list[0]).size

print('Total image count:', num_total)
print("Image dimensions:", image_width, "x", image_height)
print("Label names:", class_names)
print("Label counts:", [len(image_files[i]) for i in range(num_class)])

image_width, image_height = 128, 128
train_datagen = ImageDataGenerator(rescale=1. / 255, validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(image_width, image_height),
    batch_size=32,
    class_mode='categorical',
    subset='training')
validation_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(image_width, image_height),
    batch_size=32,
    class_mode='categorical',
    subset='validation')

# use pre trainned model
# Load VGG16 model
vgg16_model = VGG16(weights='imagenet', include_top=False, input_shape=(image_width, image_height, 3))
for layer in vgg16_model.layers:
    layer.trainable = False

# Build new model for transfer learning with VGG16
model = Sequential()
model.add(vgg16_model)
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_class, activation='softmax'))

# Compile model with Adam optimizer
model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.0001), metrics=['accuracy'])

# Train model with fine-tuning
model.fit(
    train_generator,
    steps_per_epoch=train_generator.n // train_generator.batch_size,
    epochs=20,
    validation_data=validation_generator,
    validation_steps=validation_generator.n // validation_generator.batch_size,
    verbose=1)

# save the model
model.save('my_model.h5')

# evaluate the model on test data
test_loss, test_acc = model.evaluate(validation_generator)

# print the test loss and accuracy
print('Test loss:', test_loss)
print('Test accuracy:', test_acc)
# Load the new image
