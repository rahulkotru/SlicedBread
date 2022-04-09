import numpy as np
import tifffile as tiff
import os
import matplotlib.pyplot as plt

class Image():

    def __init__(self):
        print("Please enter file directory")
        self.path=input()
        print(self.path)
        if (os.path.exists(self.path)):
            mainImg=tiff.imread(self.path)
            self.height,self.width=mainImg.shape
            self.removeExt()
            print("Filename is: "+self.name)


        

    def tile(self,row, col):
        self.row = row
        self.col = col

    def removeExt(self):
        base=os.path.basename(self.path)
        name=os.path.splitext(base)[0]
        self.name=name



img=Image()


