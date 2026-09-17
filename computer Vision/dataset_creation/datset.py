import cv2 as cv
import os

output_path = r"F:\quantanics\computer Vision\dataset_creation\output\jeeva2"

if not os.path.exists(output_path):
    os.makedirs(output_path)

video = cv.VideoCapture(0)
frame_count = 0    
save_count = 0      

while True:
    ret, frame = video.read()
    if not ret:
        break

    cv.imshow("Video", frame)
    frame_count += 1

    # Ignore first 9 frames
    if frame_count > 10 and save_count < 108:
        cv.imwrite(os.path.join(output_path, f"frame_{save_count}.jpg"), frame)
        save_count += 1

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
