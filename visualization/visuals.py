import numpy as np
import matplotlib.pyplot as plt


def plot(history, epochs, save=False):
    print("Started Plotting .....")
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, epochs), history.history["loss"], label="train_loss")
    plt.plot(np.arange(0, epochs), history.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, epochs), history.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, epochs), history.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    print("Completed Plotting .....")
    if save:
        print("Started saving .....")
        plt.savefig(r"plots")
        print("Completed saving .....")
