import cv2

# Load an image
image = cv2.imread(r"D:\OpenCV\Blurring\MeadianBlur\Butterfly.png")

# Apply median blur with a kernel size of 3x3
blurred_image = cv2.medianBlur(image, 11)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
