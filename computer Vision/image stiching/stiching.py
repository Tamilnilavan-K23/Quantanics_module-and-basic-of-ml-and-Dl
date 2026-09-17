import numpy as np
import cv2
import glob
import imutils

image_paths = glob.glob(r'F:\quantanics\computer Vision\image stiching\unstiching image\*.jpg')

imgs = []

for i in range(len(image_paths)):
    img = cv2.imread(image_paths[i])
    img = cv2.resize(img, (700,700))
    imgs.append(img)
    imgs[i] = cv2.resize(imgs[i], (0, 0), fx=0.4, fy=0.4)

cv2.imshow('1', imgs[0])
cv2.imshow('2', imgs[1])
cv2.imshow('3', imgs[2])

stitchy = cv2.Stitcher.create()
status, output = stitchy.stitch(imgs)

if status != cv2.Stitcher_OK:
    print("Stitching isn't successful")
else:
    print('Your Panorama is ready!!!')

    # Post-processing steps
    output = cv2.copyMakeBorder(output, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0, 0, 0))
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

    contours = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)

    mask = np.zeros(thresh_img.shape, dtype="uint8")
    x, y, w, h = cv2.boundingRect(areaOI)
    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

    minRectangle = mask.copy()
    sub = mask.copy()

    while cv2.countNonZero(sub) > 0:
        minRectangle = cv2.erode(minRectangle, None)
        sub = cv2.subtract(minRectangle, thresh_img)

    contours = cv2.findContours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(areaOI)
    output = output[y:y + h, x:x + w]

    cv2.imshow('Final Result', output)
    cv2.imwrite("final.png",output)
cv2.waitKey(0)
cv2.destroyAllWindows()
