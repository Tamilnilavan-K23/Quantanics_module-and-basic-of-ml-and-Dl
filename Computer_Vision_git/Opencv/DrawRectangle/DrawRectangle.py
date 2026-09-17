import cv2

image = cv2.imread(r"D:\Quantanics\Saran Sir\OpenCV\DrawRectangle\Dog.png")
start_point = (50, 50)
end_point = (200, 150)
color = (255, 0, 0)  # Blue color in BGR format
thickness = 2
cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow("Draw Rectangle", image)
