import matplotlib.pyplot as plt
import numpy as np


def plot_time_series(t, signals, labels, title, fname=None):
plt.figure(figsize=(8,4))
for s,l in zip(signals, labels):
plt.plot(t, s, label=l)
plt.xlabel('Time (s)')
plt.legend()
plt.title(title)
plt.grid(True)
if fname:
plt.tight_layout()
plt.savefig(fname)
else:
plt.show()




def rmse(a,b):
return np.sqrt(((a-b)**2).mean())
