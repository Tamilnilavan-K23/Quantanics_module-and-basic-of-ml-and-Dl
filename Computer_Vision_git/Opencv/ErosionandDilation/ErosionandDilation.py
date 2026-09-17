import cv2
import numpy as np

# Load a binary image
image = cv2.imread(r"D:\OpenCV\ErosionandDilation\BinaryImage.png", cv2.IMREAD_GRAYSCALE)

# Define a structuring element (3x3 square)
kernel = np.ones((3, 3), np.uint8)

# Apply erosion and dilation
eroded_image = cv2.erode(image, kernel, iterations=1)
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display the original, eroded, and dilated images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
