import tensorflow as tf


def load_data(directory, img_size, batch_size):
    print("loading data .....")

    train_ds = tf.keras.utils.image_dataset_from_directory(
        directory,
        label_mode='categorical',
        batch_size=batch_size,
        image_size=img_size,
        seed=42,
        validation_split=0.2,
        subset='training',
    )

    valid_ds = tf.keras.utils.image_dataset_from_directory(
        directory,
        label_mode='categorical',
        batch_size=batch_size,
        image_size=img_size,
        seed=42,
        validation_split=0.2,
        subset='validation',
    )

    classes = len(train_ds.class_names)

    class_names = train_ds.class_names

    print("completed loading data .....")

    return train_ds, valid_ds, classes
