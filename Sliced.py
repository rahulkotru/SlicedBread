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



        

    def tile(self):
        print("This method will create tiles of dimension defined by the user")
        print("The current dimension of the image is: "+ self.height + " x " + self.width)
        print("Please enter valid tile dimensions(example: 225, 256, 512,1024)")


    def removeExt(self):
        base=os.path.basename(self.path)
        name=os.path.splitext(base)[0]
        self.name=name



img=Image()
img.tile()
#D:\20_SanFrancisco\San Francisco\Flipped/T11.tif
