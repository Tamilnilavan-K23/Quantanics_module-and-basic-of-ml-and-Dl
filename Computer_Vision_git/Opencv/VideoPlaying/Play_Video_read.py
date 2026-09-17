import cv2

# Open a video file or capture device
video_path = 'videofile.mp4'  # Replace with the path to your video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file.")
    exit()

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if no more frames are available
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Check if the user pressed the 'q' key to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
