from PIL import Image
import numpy as np
Image.MAX_IMAGE_PIXELS=100000000000
import tifffile as tiff

img1=Image.open("D:/28_GitHub/SlicedBread/Tester/Test.tif")
print(img1.format)
img2=np.asarray(img1)
tiff.imsave("hi.tif",img2)
12345678