import cv2
import numpy as np

# Process:
'''
1. The process is same only we'll read
video as frames in a loop
2. Convert frames into hsv color model
so working becomes easy
3. Detect custom color objects using color segmentation -->
return coordinates of objects --> (x,y,w,h)
4. Draw rectangles around them in the frames
5. If found then we start saving the clip from there
until the object is in the frame
'''
# 0 - default webcam
# 1 - ext. webcam
# path - video file path
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(filename=r"funny_test_video.mp4")

# init video processing packages by cv2 for output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, dsize=(500, 700))
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Custom lower and upper limits for the color #ff1a8c (pink)
    lower_limit = np.array([150, 100, 100])  # Adjust these values as needed
    upper_limit = np.array([180, 255, 255])  # Adjust these values as needed

    # Create a mask for the custom color
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    # For making a bounding box
    bbox = cv2.boundingRect(mask)

    # If we get a bounding box, use it to draw a rectangle on the image
    if bbox is not None:
        print("Object detection running:", bbox)
        x, y, w, h = bbox
        if w != 0 and h != 0:
            print("Custom color objects in frame at ")
            frame = cv2.rectangle(frame,
                                  (x, y),
                                  (x + w, y + h),
                                  (255, 26, 140), 2)  # Color code #ff1a8c
            # Writing the frames into an output video file
            out.write(frame)
        else:
            print("Object not detected")

    cv2.imshow("Video Frame", frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        cap.release()
        # After we release our webcam, we also release the output
        out.release()
        break

cv2.destroyAllWindows()
