import cv2 as cv
image_path=r"C:\Users\Tamil\OneDrive\Pictures\png-transparent-olympic-games-computer-icons-sport-athlete-sports-activities-miscellaneous-text-racing.png"
image=cv.imread(image_path)

if image is not None:
    cv.imshow("Loaded Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

cv.imwrite("readimage.png", image)  