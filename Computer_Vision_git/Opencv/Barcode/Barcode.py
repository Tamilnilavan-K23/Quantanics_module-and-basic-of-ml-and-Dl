import cv2
from pyzbar.pyzbar import decode

# Load the image
image_path = 'Barcode2.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Decode barcodes from the grayscale image
barcodes = decode(gray_image)

# Loop through the detected barcodes and print the data
for barcode in barcodes:
    data = barcode.data.decode('utf-8')
    print(f"Barcode Type: {barcode.type}, Data: {data}")

    # Draw a bounding box around the barcode
    points = barcode.polygon
    if len(points) > 4:
        hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
        cv2.polylines(image, [hull], True, (0, 255, 0), 2)
    else:
        cv2.polylines(image, [points], True, (0, 255, 0), 2)

# Display the image with detected barcodes
cv2.imshow('Detected Barcodes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
