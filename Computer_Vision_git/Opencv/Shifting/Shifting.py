import cv2
import numpy as np

# Load an image
image = cv2.imread(r"D:\OpenCV\Shifting\Tiger.jpg")

# Get image dimensions
height, width = image.shape[:2]

# Define shift amounts
shift_x = 50
shift_y = -30

# Create the transformation matrix for shifting
M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])

# Perform shifting
shifted_image = cv2.warpAffine(image, M, (width, height))

# Display the original and shifted images
cv2.imshow('Original Image', image)
cv2.imshow('Shifted Image', shifted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
