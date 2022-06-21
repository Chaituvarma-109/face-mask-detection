import tensorflow as tf


augment = tf.keras.Sequential([
        tf.keras.layers.RandomFlip(),
        tf.keras.layers.RandomRotation(0.2, fill_mode='nearest'),
        tf.keras.layers.RandomHeight(factor=0.2),
        tf.keras.layers.RandomWidth(factor=0.2),
    ])
