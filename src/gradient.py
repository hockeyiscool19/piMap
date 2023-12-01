import matplotlib
matplotlib.use('TkAgg')

import rasterio
import numpy as np
import matplotlib.pyplot as plt
import random

try:
    dataset = np.load("src/gis/map.npy")
    print("Loaded")
except Exception as e:
    print(f"Could not load data: {e}")
"""
Gradient ascent:
    Track coordinates array
    Pick min rise: 2m
    1. Pick a random point on the map. 
    2. Enter loop
    3. Find four adjacent points
    4. Go to highest coordinate. Append to coordinates
"""

class Gradient:
    def __init__(self, dataset, minRise, stepSize):
        """
        :params
            dataset: tif map
            minrise: minimum rise to continue algorithm
        """
        self.paths = []
        self.map = dataset
        print(self.map)
        self.minRise = minRise
        self.vertical = dataset.shape[1]
        self.horazontal = dataset.shape[2]
        print(self.vertical, self.horazontal)
    
    @staticmethod
    def metersToFeet(elevation):
        elev = elevation * 3.28084
        return elev
    def ascent(self, stepSize):
        vert = random.randrange(0, self.vertical)
        hor = random.randrange(0, self.horazontal)  # Corrected spelling
        path, currRise = [], self.minRise + 1
        elevations = []

        while currRise > self.minRise:
            print(f"vert, hor {vert, hor}")
            elev = self.metersToFeet(self.map[0][vert][hor])
            elevations.append(elev)
            path.append([hor, vert])  # Corrected this line
            newPositions = [(hor-stepSize, vert), (hor, vert-stepSize), (hor+stepSize, vert), (hor, vert+stepSize)]
            print(f"possible Options: {newPositions}")
            newRise, newVert, newHor = float("-inf"), -1, -1

            for h, v in newPositions:
                print(h, v)
                if v >= 0 and h >= 0 and v < self.vertical and h < self.horazontal:  # Corrected spelling
                    rise = self.map[0][v][h] - self.map[0][vert][hor]
                    print("Rise ", rise)
                    if rise > newRise:
                        newRise, newVert, newHor = rise, v, h

            currRise, vert, hor = newRise, newVert, newHor

        elev = self.metersToFeet(self.map[0][vert][hor])
        print(f"Highest elevation achieved: {elev}")
        return path, elevations, elev
 
    def displayMap(self, path):
        plt.imshow(self.map[0], cmap='Spectral')
        x,y = zip(*path)
        plt.plot(x,y,color="black", linewidth=2)
        plt.show()
    
    def multiDisplay(self, paths):
        plt.imshow(self.map[0], cmap='Spectral')
        for path in paths:
            x,y = zip(*path)
            plt.plot(x,y,color="black", linewidth=2)
        plt.savefig("images/ascents.png")
        plt.show()

    def miniDisplay(self, path):
        plt.imshow(self.map[0], cmap='Spectral')
        x, y = zip(*path)
        plt.plot(x, y, color="black", linewidth=2)
        center_x = (max(x) + min(x)) / 2
        center_y = (max(y) + min(y)) / 2
        padding = 100  # Adjust as needed
        half_side = max(max(x) - min(x), max(y) - min(y)) / 2 + padding
        plt.xlim(center_x - half_side, center_x + half_side)
        plt.ylim(center_y - half_side, center_y + half_side)
        plt.gca().invert_yaxis()
        plt.savefig("images/ascents.png")
        plt.show()

    def multiAscent(self, tries, stepSize):
        paths, elevations, highestPoints  = [], [], []
        for i in range(tries):
            path, elev, highestPoint = self.ascent(stepSize)
            paths.append(path)
            elevations.append(elev)
            highestPoints.append(highestPoint)
        print(np.max(highestPoints))
        return paths, elevations, highestPoints
    


if __name__=="__main__":
    gradient = Gradient(dataset, 0, 1)
    paths, elevations, highestPoints = gradient.multiAscent(200, 4)
    # display all ascents
    gradient.multiDisplay(paths)
    # Longest path
    longest = max(paths, key=lambda coll: len(coll))
    print(longest)
    gradient.miniDisplay(longest)
