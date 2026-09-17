import cv2 as cv
from matplotlib import pyplot as plt

image_path1 = r"F:\quantanics\computer Vision\bitwise\OR\Image1.jpg"
image1 = cv.imread(image_path1) 
image_path2 = r"F:\quantanics\computer Vision\bitwise\OR\Image2.jpg"
image2 = cv.imread(image_path2)

def bitwise_or(image1,image2):
    or_image = cv.bitwise_or(image1, image2)    
    plt.subplot(221), plt.imshow(image1), plt.title('Image 1')
    plt.subplot(222), plt.imshow(image2), plt.title('Image 2')  
    plt.subplot(223), plt.imshow(or_image), plt.title('OR Image')
    plt.show()

if image1 is not None and image2 is not None:
    bitwise_or(image1, image2)