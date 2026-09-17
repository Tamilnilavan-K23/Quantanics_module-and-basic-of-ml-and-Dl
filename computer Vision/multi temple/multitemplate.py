import cv2 as cv
import numpy as np

image_color=cv.imread(r"F:\quantanics\computer Vision\multi temple\main.jpg")

gray=cv.cvtColor(image_color,cv.COLOR_BGR2GRAY)

template=cv.imread(r"F:\quantanics\computer Vision\multi temple\template.jpg",0)

w,h=template.shape[::-1]

res=cv.matchTemplate(gray,template,cv.TM_CCOEFF_NORMED)

tre=0.8
loc=np.where(res>=tre)

for pt in zip(*loc[::-1]):
    cv.rectangle(image_color,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv.imshow('Multiple Object',image_color)
cv.waitKey(0)
cv.destroyAllWindows()