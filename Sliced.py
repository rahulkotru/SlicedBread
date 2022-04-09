import numpy as np
import tifffile as tiff
import os
import matplotlib.pyplot as plt

class Image():

    def __init__(self,path):
        self.path=path
        mainImg=tiff.imread(self.path)
        self.height,self.width=mainImg.shape
        print(self.height)
        print(self.width)


    def tile(self,row, col):
        self.row = row
        self.col = col




img=Image("D:/20_SanFrancisco/San Francisco/Flipped/T11.tif")

