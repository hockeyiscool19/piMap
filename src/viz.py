import matplotlib
matplotlib.use('TkAgg')

import rasterio
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    dataset = np.load("src/gis/map.npy")
    print(dataset.shape)
    print(dataset[0])
    plt.imshow(dataset[0], cmap='Spectral')
    plt.savefig("images/topology.png")
    plt.show()

