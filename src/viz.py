import matplotlib
matplotlib.use('TkAgg')

import rasterio
import numpy as np
import matplotlib.pyplot as plt

dataset = np.load("gis/map.npy")
print(dataset.shape)
print(dataset[0])
plt.imshow(dataset[0], cmap='Spectral')
plt.show()

