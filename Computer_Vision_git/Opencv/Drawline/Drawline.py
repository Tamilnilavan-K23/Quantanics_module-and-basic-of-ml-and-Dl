import cv2

image = cv2.imread(r"D:\Quantanics\Saran Sir\OpenCV\Drawline\flower.png")
start_point = (50, 50)
end_point = (200, 200)
color = (0, 255, 0)  # Green color in BGR format
thickness = 2
cv2.line(image, start_point, end_point, color, thickness)
cv2.imshow("line_drawn", image)

