import cv2

# Load an image
image = cv2.imread('image1.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error loading image.")
    exit()

# Perform Bitwise NOT operation
result = cv2.bitwise_not(image)

# Display the original image and the result
cv2.imshow('Original Image', image)
cv2.imshow('Bitwise NOT Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
