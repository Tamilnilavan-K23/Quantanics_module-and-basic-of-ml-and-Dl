import cv2

# Load a noisy image
noisy_image = cv2.imread(r"D:\Quantanics\Saran Sir\OpenCV\Denoising of colored Image\NoisyImage1.png")

# Apply Non-Local Means Denoising
denoised_image = cv2.fastNlMeansDenoisingColored(noisy_image, None, 15, 15, 7, 21)

# Display the original and denoised images
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
