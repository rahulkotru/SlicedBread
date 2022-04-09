import numpy as np
import tifffile as tiff
import os
import matplotlib.pyplot as plt
from PIL import Image
Image.MAX_IMAGE_PIXELS=100000000000

class Picture():

    def __init__(self):
        print("Please enter file directory")
        self.path=input()
        print(self.path)
        if (os.path.exists(self.path)):
            mainImg=tiff.imread(self.path)
            self.height,self.width,_=mainImg.shape
            self.removeExt()
            print("Filename is: "+self.name)


    def removeExt(self):
        base=os.path.basename(self.path)
        name=os.path.splitext(base)[0]
        self.name=name
        

    def tile(self,size):
        #print("This method will create tiles of dimension defined by the user")
        print("The current dimension of the image is:  {}  x  {}".format(self.height,self.width))
        print("Please enter valid tile dimensions(example: 225, 256, 512,1024)")
        print("Total patches possible are: {}".format((self.height//size)+(self.width//size)))
        print("Press Y to Continue\nPress N to quit")
        proceed=input()
        if(proceed.lower()=='n'):
            print("Alright dubby")
        


    def tile_patch(imag,l,t,r,b):
        cropped=imag.crop((l,t,r,b))
        convert_to_array=np.array(cropped)
        return convert_to_array







img=Picture()
img.tile(64)
#D:\20_SanFrancisco\San Francisco\Flipped/T11.tif
