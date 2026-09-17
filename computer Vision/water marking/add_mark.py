import cv2
import numpy as np
import glob
import os

logo = cv2.imread("mylogo.png")
logo_height, logo_width, _ = logo.shape

# Resize the logo to a smaller size
new_logo_width = int(logo_width * 0.5)  # Adjust the scale factor as needed
new_logo_height = int(logo_height * 0.5)
logo_resized = cv2.resize(logo, (new_logo_width, new_logo_height))

images_path = glob.glob("1.jpg")

print("Adding watermark")
for img_path in images_path:
    img = cv2.imread(img_path)
    h_img, w_img, _ = img.shape

    # Get the center of the original image. It's the location where we will place the watermark
    center_y = int(h_img / 2)
    center_x = int(w_img / 2)

    # Resize the logo to match the dimensions of the roi
    logo_resized = cv2.resize(logo_resized, (w_img, h_img))

    # Blend the resized logo with the image using alpha channel
    result = cv2.addWeighted(img, 1, logo_resized, 0.3, 0)

    # Get filename and save the image
    filename = os.path.basename(img_path)
    cv2.imwrite("watermarked_" + filename, result)

print("Watermark added to all the images")
