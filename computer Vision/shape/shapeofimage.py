import cv2 as cv
import numpy as np

image_path= r"C:\Users\Tamil\OneDrive\Pictures\png-transparent-olympic-games-computer-icons-sport-athlete-sports-activities-miscellaneous-text-racing.png"
image = cv.imread(image_path)

def print_shape(image):
    if image is not None:
       cv.line(image, (0, 0), (100, 10), (255, 0, 0), 2 )
       cv.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 2)
       cv.circle(image, (150, 150), 50, (0, 0, 255), 2)
       cv.ellipse(image, (300, 150), (50, 100), 0, 0, 180, (255, 255, 0), 2)
       cv.arrowedLine(image, (400, 150), (500, 200), (255, 0, 255), 2)
       cv.polylines(image, [np.array([[600, 100], [700, 50], [800, 150], [750, 200]], np.int32)], True, (0, 255, 255), 2)
       cv.fillPoly(image, [np.array([[900, 100], [950, 50], [1000, 150], [950, 200]], np.int32)], (255, 128, 0))    
       cv.imshow("Image with Shapes", image)    
       cv.waitKey(0)
       cv.destroyAllWindows()
       cv.imwrite("shapes_image.png", image)
    else:
        print("Failed to load the image.")

#cv.imwrite("shapes_image.png", image)

print_shape(image)  