import cv2 as cv

image_path=r"C:\\Users\\Tamil\\OneDrive\\Pictures\\png-transparent-olympic-games-computer-icons-sport-athlete-sports-activities-miscellaneous-text-racing.png"
image =cv.imread(image_path)

def denoise_image(image):
    
    denoised_image = cv.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    cv.imshow("Original Image", image)
    cv.imshow("Denoised Image", denoised_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("denoised_image.png", denoised_image)

if image is not None:
    denoise_image(image)