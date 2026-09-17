import cv2 as cv
from matplotlib import pyplot as plt
image_path1 = r"F:\quantanics\computer Vision\bitwise_and\AND\Image1.jpg"
image1 = cv.imread(image_path1)

image_path2=r"F:\quantanics\computer Vision\bitwise_and\AND\image2.jpg"
image2 = cv.imread(image_path2)

def bitwise_and_images(image1, image2):
    if image1.shape != image2.shape:
        raise ValueError("Images must have the same dimensions for bitwise AND operation.")
    
    bitwise_and_image = cv.bitwise_and(image1, image2,mask=None)
    #cv.imshow("Image 1", image1)
    #cv.imshow("Image 2", image2)
    #cv.imshow("Bitwise AND Image", bitwise_and_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    #cv.imwrite("bitwise_and_image.png", bitwise_and_image)
    plt.imshow(cv.cvtColor(bitwise_and_image, cv.COLOR_BGR2RGB))
    plt.axis('off') 
    plt.show()

if image1 is not None and image2 is not None:
    bitwise_and_images(image1, image2)
