import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Load the image
image_path = r'F:\quantanics\computer Vision\bar coder scanner\image3.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Decode barcodes from the grayscale image
barcodes = decode(gray_image)

# Loop through the detected barcodes and print the data
for barcode in barcodes:
    data = barcode.data.decode('utf-8')
    print(f"Barcode Type: {barcode.type}, Data: {data}")

    # Get bounding box coordinates
    x, y, w, h = barcode.rect
    image=cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Optionally display data near the barcode
    image=cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Display the image with detected barcodes
cv2.imshow('Detected Barcodes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
