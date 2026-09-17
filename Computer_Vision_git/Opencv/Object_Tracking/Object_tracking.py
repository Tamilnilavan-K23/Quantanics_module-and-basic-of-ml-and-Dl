import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    # Convert the target color to HSV
    target_color_rgb = np.uint8([[[0, 153, 204]]])  # RGB value for #0099cc
    target_color_hsv = cv2.cvtColor(target_color_rgb, cv2.COLOR_RGB2HSV)

    # Define a color range based on the target color in HSV
    lower_color = np.array([target_color_hsv[0][0][0] - 10, 100, 100])
    upper_color = np.array([target_color_hsv[0][0][0] + 10, 255, 255])

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask based on the color range
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:  # Adjust this threshold based on the object size
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Object Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
