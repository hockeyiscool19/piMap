import matplotlib
matplotlib.use('TkAgg')

import rasterio
import numpy as np
import matplotlib.pyplot as plt
from numpy import save


if __name__=="__main__":
    file1 = rasterio.open("gis/USGS_13_n39w107_20220331.tif")
    dataset1 = file1.read()

    file2= rasterio.open("gis/USGS_13_n40w107_20220216.tif")
    dataset2 = file2.read()

    print(dataset1.shape, dataset2.shape)
    newFile = np.concatenate((dataset1, dataset2), axis=1)
    print(newFile.shape)
    save("gis/map.npy", newFile)
    print("wrote to disk")
