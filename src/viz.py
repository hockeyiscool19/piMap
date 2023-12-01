import matplotlib
matplotlib.use('TkAgg')

import rasterio
import numpy as np
import matplotlib.pyplot as plt


file = rasterio.open("gis/USGS_13_n39w107_20220331.tif")
dataset = file.read()
print(dataset.shape)
print(dataset[0])
plt.imshow(dataset[0], cmap='Spectral')
plt.show()

