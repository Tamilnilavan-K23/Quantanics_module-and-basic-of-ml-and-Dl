""""

import requests
import cv2
import numpy as np
import imutils


url = "http://192.168.1.39:8080/shot.jpg"

path=r"F:\quantanics\computer Vision\android camera\output video"
fourcec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(path + r"\output.avi", fourcec, 20.0, (1000, 1800))
while True:
			img_resp = requests.get(url)
			img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
			img = cv2.imdecode(img_arr, -1)
			img = imutils.resize(img, width=1000)  # Only width used, height auto-adjusted
			resized_height, resized_width = img.shape[:2]

		# Resize again if frame_height doesn't match (to avoid mismatch error)
			if (resized_width, resized_height) != (1000, 1800):
				img = cv2.resize(img, (1000, 1800))
			out.write(img)
			cv2.imshow("Android_cam", img)
			if cv2.waitKey(1) == 27:
				break

out.release()
cv2.destroyAllWindows()
"""

import requests
import cv2
import numpy as np
import imutils
import os

url = "http://192.168.1.39:8080/shot.jpg"
path = r"F:\quantanics\computer Vision\android camera\output video"
os.makedirs(path, exist_ok=True)  # Create folder if not exists

# Grab first frame to determine correct size
img_resp = requests.get(url)
img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
img = cv2.imdecode(img_arr, -1)
img = imutils.resize(img, width=1000)
frame_height, frame_width = img.shape[:2]

# Create VideoWriter with actual size
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(os.path.join(path, "output2.avi"), fourcc, 10.0, (frame_width, frame_height))

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000)

    # Ensure size matches
    img = cv2.resize(img, (frame_width, frame_height))

    out.write(img)
    cv2.imshow("Android_cam", img)

    if cv2.waitKey(1) == 27:  # ESC key to exit
        break

out.release()
cv2.destroyAllWindows()
