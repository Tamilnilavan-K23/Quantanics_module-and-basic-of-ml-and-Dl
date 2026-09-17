import cv2 as cv
from matplotlib import pyplot as plt

image_path= r"C:\Users\Tamil\OneDrive\Pictures\png-transparent-olympic-games-computer-icons-sport-athlete-sports-activities-miscellaneous-text-racing.png"
image = cv.imread(image_path)
def resize_image(image):

   resized_image = cv.resize(image, (100, 100), interpolation=cv.INTER_NEAREST)
   plt.figure(figsize=(8, 6))
   plt.subplot(1, 2, 1)
   plt.title("Original Image")
   plt.axis("off")
   plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
   plt.subplot(1, 2, 2)
   plt.title("Resized Image")
   plt.axis("off")
   plt.imshow(cv.cvtColor(resized_image, cv.COLOR_BGR2RGB))
   plt.axis("off")
   plt.show()

   cv.imwrite("resized_image.png", resized_image)
if image is not None:
    resize_image(image)