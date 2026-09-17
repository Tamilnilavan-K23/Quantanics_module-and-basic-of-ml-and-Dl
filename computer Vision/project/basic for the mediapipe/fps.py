import cv2

cap=cv2.VideoCapture(0)
actual_fps=cap.get(cv2.CAP_PROP_FPS)
print("Actual FPS:", actual_fps)
