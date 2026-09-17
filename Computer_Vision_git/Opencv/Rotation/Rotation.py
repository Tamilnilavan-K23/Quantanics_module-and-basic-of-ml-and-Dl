import cv2
import numpy as np

# Load an image
image = cv2.imread("D:\OpenCV\Rotation\Tiger.jpg")

# Get image dimensions
height, width = image.shape[:2]

# Define rotation angle (positive values are counterclockwise)
angle = 45

# Define rotation center
center = (width // 2, height // 2)

# Get rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)

# Perform rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
