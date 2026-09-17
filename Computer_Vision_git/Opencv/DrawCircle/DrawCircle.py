import cv2

image = cv2.imread(r"D:\Quantanics\Saran Sir\OpenCV\DrawCircle\Dog.png")
center = (150, 150)
radius = 50
color = (0, 0, 255)  # Red color in BGR format
thickness = 3
cv2.circle(image, center, radius, color, thickness)
cv2.imshow('Circle_drawn', image)
