import cv2 as cv
image_path= r"C:\Users\Tamil\OneDrive\Pictures\png-transparent-olympic-games-computer-icons-sport-athlete-sports-activities-miscellaneous-text-racing.png"
image = cv.imread(image_path)
def text_image(image):
    cv.putText(image, "Hello, quantianics", (50, 50), cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
    cv.imshow("Image with Text", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("text_image.png", image) 

if image is not None:
    text_image(image)