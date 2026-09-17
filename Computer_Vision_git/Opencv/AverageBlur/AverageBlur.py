import cv2

# Load an image
image = cv2.imread(r"D:\Quantanics\Saran Sir\OpenCV\Blurring\AverageBlur\flower.png")

# Define the kernel size for average blur
kernel_size = (5, 5)

# Apply average blur
blurred_image = cv2.blur(image, kernel_size)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
