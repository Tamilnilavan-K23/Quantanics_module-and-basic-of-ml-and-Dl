import cv2
import numpy as np

# Create a blank image
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Define text string and position
text = "Hello, OpenCV!"
position = (100, 200)

# Choose font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
color = (255, 255, 255)  # White color in BGR format
thickness = 2

# Draw the text on the image
cv2.putText(image, text, position, font, font_scale, color, thickness)

# Display the image
cv2.imshow('Text Drawing', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
