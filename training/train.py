import tensorflow as tf

from model.model import build_model


def train(train_ds, valid_ds, epochs, lr, classes):
    print("started training....")
    model = build_model(classes)
    opt = tf.keras.optimizers.Adam(learning_rate=lr, decay=lr / epochs)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    history = model.fit(train_ds, epochs=epochs, validation_data=valid_ds)
    print("completed training....")
    return history
