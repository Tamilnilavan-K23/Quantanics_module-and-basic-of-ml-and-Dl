import cv2 as cv
from matplotlib import pyplot as plt 

image_path1 = r"F:\quantanics\computer Vision\bitwise\NOT\Image1.jpg"
image1 = cv.imread(image_path1)
image_path2 = r"F:\quantanics\computer Vision\bitwise\NOT\Image2.jpg"
image2 = cv.imread(image_path2)

def bitwise_not(image1,image2):

    not_image1=cv.bitwise_not(image1)
    not_image2=cv.bitwise_not(image2)

    plt.subplot(221),plt.imshow(image1),plt.title('Image 1')
    plt.subplot(222),plt.imshow(not_image1),plt.title('NOT Image  1')
    plt.subplot(223),plt.imshow(image2),plt.title('Image 2')
    plt.subplot(224),plt.imshow(not_image2),plt.title('NOT Image 2')

    plt.show()

if image1 is not None and image2 is not None :
    bitwise_not(image1, image2)