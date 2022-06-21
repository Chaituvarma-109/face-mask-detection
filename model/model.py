import tensorflow as tf

from preprocessing.preprocess import augment


def get_basemodel():
    return tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')


def build_model(classes):
    print("building model...")
    base_model = get_basemodel()

    for layer in base_model.layers:
        layer.trainable = False

    inputs = tf.keras.Input(shape=(224, 224, 3))
    x = augment(inputs)
    x = base_model(x, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(128, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    x = tf.keras.layers.Dense(units=classes, activation="softmax")(x)
    model = tf.keras.Model(inputs=inputs, outputs=x)

    print("completed building model...")

    return model


def save_model(model, path_to_save):
    model.save(path_to_save+"mask_detector.model", save_format="h5")
