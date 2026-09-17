import cv2 as cv

image_path= r"C:\\Users\\Tamil\\OneDrive\\Pictures\\png-transparent-olympic-games-computer-icons-sport-athlete-sports-activities-miscellaneous-text-racing.png"
image = cv.imread(image_path)

def edge_detection(image):

    gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    blurr=cv.GaussianBlur(gray_image,(5,5),0)
    edges=cv.Canny(blurr,100,200)
    cv.imshow("Original Image",image)
    cv.imshow("Edge Detected Image",edges)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("edge_detected_image.png", edges)

if image is not None:
    edge_detection(image)