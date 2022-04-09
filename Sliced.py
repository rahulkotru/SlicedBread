import numpy as np
import tifffile as tiff
import os
import matplotlib.pyplot as plt
from PIL import Image
Image.MAX_IMAGE_PIXELS=100000000000
from tqdm import tqdm

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
        self.image=Image.open(self.path)
        print("The current dimension of the image is:  {}  x  {}".format(self.height,self.width))
        print("Please enter valid tile dimensions(example: 225, 256, 512,1024)")
        patchX,patchY=self.height//size, self.width//size
        totalPatch=patchX+patchY
        print("Total patches possible are: {}".format((self.height//size)+(self.width//size)))
        print("Press Y to Continue\nPress N to quit")
        proceed=input()
        if(proceed.lower()=='n'):
            print("Alright dubby")
            return
        elif(proceed.lower()=='y'):
            print("Proceeding to tile input into tiles of dimension {}x{}".format(size,size))
            pathname=os.path.dirname(self.path)
            finalPath=os.path.join(pathname,self.name)
            if not os.path.exists(finalPath):
                os.makedirs(finalPath)
            pbar=tqdm(total=(self.height//size)+(self.width//size) ,desc='Creating Tiles')
            left,top,right,bottom=0,0,0,0
            count=0
            for i in range((self.height//size)):
                for j in range((self.width//size)):
                    print('hi')
                    left=j*size+j 
                    top=i*size+i
                    right=left+size
                    bottom=top+size
                    count+=1
                    self.tilePatch(left,top,right,bottom,finalPath,count)
                    pbar.update(1)
                    
                    #print('\n{}.tif'.format(count),'has been saved.')
        


    def tilePatch(self,l,t,r,b,path,c):
        cropped=self.image.crop((l,t,r,b))
        convertToArray=np.array(cropped)
        print(convertToArray)
        tiff.imsave(path+'/{}.tif'.format(c),convertToArray)







img=Picture()
img.tile(64)
#D:\20_SanFrancisco\San Francisco\Flipped/T11.tif

#D:\28_GitHub\SlicedBread\Tester\Test.tif