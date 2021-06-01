from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle


def plot_confusion_matrix(y_test, y_pred, normalize=False, title=None, cmap=plt.cm.Blues):
    classes = ["positive", "negative"]
    np.set_printoptions(precision=2)

    title = 'Confusion Matrix'

    # Compute confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)

    # Show all ticks
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
	# load in data
	heart_attack_df = pd.read_csv("generated_dataset.csv")

	# randomize rows to prevent overfitting
	heart_attack_df = heart_attack_df.sample(frac=1)

	# convert dataset to numpy to be fed to the model
	dataset = heart_attack_df.to_numpy()

	X = dataset[:, :-1]
	y = dataset[:, -1]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

	# train model
	gnb = GaussianNB()
	y_pred = gnb.fit(X_train, y_train).predict(X_test)

	# test model
	print("Gaussian Bayes heart attack classifier accuracy: %.2f%%" % (float((y_test == y_pred).sum()) / X_test.shape[0] * 100))
	plot_confusion_matrix(y_test, y_pred)

	# export model to pickle file
	pickle.dump(gnb, open("gaussian_bayes_model.pickle", 'wb'))