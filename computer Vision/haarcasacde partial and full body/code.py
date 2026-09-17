import cv2

# Load the full body and upper body cascade classifiers
full_body_cascade = cv2.CascadeClassifier('haarcascades_fullbody.xml')
upper_body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
lower_body_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

# Function to detect and draw bodies
def detect_and_draw_bodies(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    full_bodies = full_body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    upper_bodies = upper_body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    lower_bodies = lower_body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in full_bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in upper_bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in lower_bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    return img

# Detect bodies in an image
image = cv2.imread('image1.jpg')
result_image = detect_and_draw_bodies(image)
cv2.imshow('Full and Lower Body Detection in Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
