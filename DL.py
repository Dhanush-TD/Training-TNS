import tensorflow as tf
from tensorflow.keras import layers, Sequential
from tensorflow.keras.applications import ResNet50

from tensorflow.keras.applications.resnet50 import preprocess_input

#1 load the dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

#2 normalizing and scaling
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0   

print("x_train shape:", x_train.shape)
print("x_test shape:", x_test.shape)

#3 build on layers
cnn=Sequential([
    layers.Input(shape=(32, 32, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

#4 compile the model
cnn.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])


#5 train the model
cnn.fit(x_train, y_train, epochs=5, validation_split=0.2)

#6 evaluate the model
test_loss, test_accuracy = cnn.evaluate(x_test, y_test)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

#transfer learning with ResNet50

x_train_resized = tf.image.resize(x_train, (224, 224))
x_test_resized = tf.image.resize(x_test, (224, 224))         

x_train_resized = preprocess_input(x_train_resized*255.0)
x_test_resized = preprocess_input(x_test_resized*255.0)

#load the ResNet50 model without the top layer
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

base_model.trainable = False  # Freeze the base model

# create the model
transfer_model=Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# compile

transfer_model.compile(optimizer='adam',
                       loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])

# train the model
transfer_model.fit(x_train_resized, y_train, epochs=5, validation_split=0.2)

# evaluate the model
test_loss, test_accuracy = transfer_model.evaluate(x_test_resized, y_test)
print("Transfer Learning Test Loss:", test_loss)
print("Transfer Learning Test Accuracy:", test_accuracy)
