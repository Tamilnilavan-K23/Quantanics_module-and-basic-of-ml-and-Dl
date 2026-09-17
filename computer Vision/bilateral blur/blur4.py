import cv2 as cv
from matplotlib import pyplot as plt

image_path=r"C:\\Users\\Tamil\\OneDrive\\Pictures\\png-transparent-olympic-games-computer-icons-sport-athlete-sports-activities-miscellaneous-text-racing.png"
image =cv.imread(image_path)

def blur(image):
    blurred_image = cv.bilateralFilter(image, 9, 75, 75)  # Using a kernel size of 9
    plt.figure(figsize=(8, 6))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.axis("off")
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title("Bilateral Blurred Image")
    plt.axis("off")
    plt.imshow(cv.cvtColor(blurred_image, cv.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
    
    cv.imwrite("bilateral_blurred_image.png", blurred_image)

if image is not None:
    blur(image)

