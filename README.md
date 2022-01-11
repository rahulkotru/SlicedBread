# Sliced Bread 

An image processing tool for data augmentation and affine transforms built using OpenCV, GDAL, tifffile, NumPy, Python

## Functionalities
### 1) Grayscale Conversion
Converts image into grayscale using OpenCV

<img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/1.jpg" width="100px">     <img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/backhand.gif" width="50px"> <img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/2.jpg" width="100px">

### 2)Image Rotation
Rotates image by order of 90 degrees

<img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/1.jpg" width="100px">     <img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/backhand.gif" width="50px"> 
<img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/3.jpg" width="100px" rotate="90 deg">

### 3) Image Resize
Downscale or Upscale an image

<img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/1.jpg" width="100px">     <img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/backhand.gif" width="50px"> 
<img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/1.jpg" width="90px" rotate="90 deg">
### 3) Vertical and Horizotal Flip
Mirrors the image along the x-axis or y-axis or both

<img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/1.jpg" width="100px">     <img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/backhand.gif" width="50px"> 
<img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/4.jpg" width="100px" rotate="90 deg"><img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/backhand.gif" width="50px"><img src="https://raw.githubusercontent.com/rahulkotru/SlicedBread/master/assets/5.jpg" width="100px" rotate="90 deg">
### 4) Channel Stacking and Tensor
Create multi-channel images or image tensors. Can be used for channel separation and channel reordering as well.
### 5) Patches Processing
Create custom image patches(tiles) to train and test Convolutional Neural Networks. Recombine patches and integrate patches with lossless conversion.
