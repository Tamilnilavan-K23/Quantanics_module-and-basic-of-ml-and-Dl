import cv2
import numpy as np

def detect_shape(cnt):
    perimeter = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
    
    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        return "Rectangle"
    elif len(approx) == 5:
        return "Pentagon"
    else:
        return "Circle"

def detect_color(hsv_image):
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    result = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
    
    return result

# Load an image
image_path = 'Image2.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Detect shapes and colors
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edges = cv2.Canny(blurred_image, 50, 150)

dilated_image = cv2.dilate(edges, kernel, iterations=1)
contours, _ = cv2.findContours(dilated_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    shape = detect_shape(contour)
    color_detected_image = detect_color(hsv_image)
    
    # Assuming color_detected_image is your color image
    gray_image = cv2.cvtColor(color_detected_image, cv2.COLOR_BGR2GRAY)
    color = "Red" if cv2.countNonZero(gray_image) > 0 else "Unknown"
    
    # Draw contour, shape, and color text
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    moment = cv2.moments(contour)
    cX = int(moment["m10"] / moment["m00"])
    cY = int(moment["m01"] / moment["m00"])
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(image, color, (cX, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Display the result
cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
