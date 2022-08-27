import argparse
import tensorflow as tf
import os
import logging

from src.utils.common import read_yaml, create_directories
from src.utils.model import log_model_summary

STAGE = "BASE MODEL CREATION"

logging.basicConfig(
    filename=os.path.join('logs', 'logs.log'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode='a'
)


augment = tf.keras.Sequential([
    tf.keras.layers.RandomFlip(),
    tf.keras.layers.RandomRotation(0.2, fill_mode='nearest'),
    tf.keras.layers.RandomHeight(factor=0.2),
    tf.keras.layers.RandomWidth(factor=0.2),
])


def get_basemodel(params: dict):
    base_model = tf.keras.applications.MobileNetV2(input_shape=params['img_shape'], include_top=False, weights='imagenet')
    for layer in base_model.layers:
        layer.trainable = False
    return base_model


def main(config_path: str) -> None:
    config = read_yaml(config_path)

    params = config['params']

    logging.info("layers defined")
    base_model = get_basemodel(params)

    inputs = tf.keras.Input(shape=tuple(params['img_shape']))
    x = augment(inputs)
    x = base_model(x, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(128, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    x = tf.keras.layers.Dense(units=2, activation="softmax")(x)

    model = tf.keras.Model(inputs=inputs, outputs=x)

    logging.info(f"base model summary:\n{log_model_summary(model)}")

    opt = tf.keras.optimizers.Adam(learning_rate=params['lr'], decay=params['lr'] / params['epochs'])
    model.compile(loss=params['loss'], optimizer=opt, metrics=params['metrics'])

    path_to_model_dir = os.path.join(
        config["data"]["local_dir"],
        config["data"]["model_dir"]
    )
    create_directories([path_to_model_dir])

    path_to_model = os.path.join(path_to_model_dir, config["data"]["init_model_file"])

    model.save(path_to_model)
    logging.info(f"model is saved at : {path_to_model}")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
