import cv2 as cv    

from matplotlib import pyplot as plt

image_path = r"F:\quantanics\Computer_Vision_git\Opencv\Contours\FindingContours\Dog.png"
image = cv.imread(image_path)

def contours_image(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    thers,binary=cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)

    contours,hiearchy=cv.findContours(binary,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    contour_image = cv.drawContours(image.copy(), contours, -1, (0, 0, 255), 2)

    plt.imshow(cv.cvtColor(contour_image, cv.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

if image is not None:
    contours_image(image)
else:
    print("Failed to load the image.")