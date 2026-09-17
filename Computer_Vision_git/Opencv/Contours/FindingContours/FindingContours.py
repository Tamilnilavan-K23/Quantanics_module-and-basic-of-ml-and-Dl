import cv2
import numpy as np

# Read an image and convert to grayscale
image = cv2.imread(r"D:\Quantanics\Saran Sir\OpenCV\Contours\FindingContours\Dog.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank image for drawing contours
contour_image = np.zeros_like(image)

# Draw contours on the blank image
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Contours', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
