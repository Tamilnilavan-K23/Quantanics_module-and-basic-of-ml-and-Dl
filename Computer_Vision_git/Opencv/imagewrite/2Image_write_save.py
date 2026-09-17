import cv2
image = cv2.imread(r"C:\Users\HP\OneDrive\Pictures\PICt2.png")
cv2.imwrite('output.png', image)  # Saves the image as a PNG file

