from loading.data_loading import load_data
from training.train import train
from visualization.visuals import plot

DIRECTORY = r"DataSet/mask_data"
CATEGORIES = ["with_mask", "without_mask"]

BATCH_SIZE = 32
IMG_SIZE = (224, 224)
INIT_LR = 1e-4
EPOCHS = 1


def main():
    train_ds, valid_ds, classes = load_data(DIRECTORY, IMG_SIZE, BATCH_SIZE)
    hist = train(train_ds, valid_ds, EPOCHS, INIT_LR, classes)
    plot(hist, EPOCHS)


if __name__ == "__main__":
    main()
