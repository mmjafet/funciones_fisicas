import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Cargar el conjunto de datos MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los datos (escalar los valores de píxeles al rango [0, 1])
x_train, x_test = x_train / 255.0, x_test / 255.0

# Crear el modelo de la red neuronal
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Aplanar la imagen de 28x28 a un vector de 784 elementos
    layers.Dense(128, activation='relu'),  # Capa oculta con 128 neuronas y activación ReLU
    layers.Dropout(0.2),  # Dropout para evitar el sobreajuste
    layers.Dense(10, activation='softmax')  # Capa de salida con 10 neuronas (una por cada clase) y activación softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
print("Entrenando la red neuronal...")
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

