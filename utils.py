# utils.py

import numpy as np
import matplotlib.pyplot as plt

def rmse(y_true, y_pred):
    """Compute Root Mean Square Error"""
    return np.sqrt(np.mean((y_true - y_pred)**2))

def plot_time_series(t, data, labels, title, fname):
    """Plot multiple time series and save the figure"""
    plt.figure(figsize=(8,4))
    for d, label in zip(data, labels):
        plt.plot(t, d, label=label)
    plt.xlabel('Time [s]')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fname)
    plt.close()
