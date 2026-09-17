import cv2

# Load an image
image = cv2.imread(r"D:\OpenCV\Scaling\Tiger.jpg")

# Define new dimensions
new_width = 800
new_height = 600

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
