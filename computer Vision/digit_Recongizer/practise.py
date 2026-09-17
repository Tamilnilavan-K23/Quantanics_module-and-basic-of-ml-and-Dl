import cv2
import numpy as np
from  tensorflow.keras.models import load_model


def predication(image,model):
    image=cv2.resize(image,(28,28))
    image=image/255
    image=image.reshape(1,28,28,1)
    predict=model.predict(image)
    pro=np.amax(predict)
    index=np.argmax(predict,axis=1)[0]

    result=index
    if pro<0.75:
        result=0
        pro=0

    return result,pro

model=load_model(r'F:\quantanics\computer Vision\digit_Recongizer\digits.h5')

img=cv2.imread(r'F:\quantanics\computer Vision\digit_Recongizer\image\7.jpg')
frame=img.copy()

frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
frame=cv2.resize(frame,(28,28))
cv2.imshow("Cropped",frame)

digit,prob=predication(frame,model)
print(f"Recognized digit: {digit} with probability: {prob:.2f}")

cv2.imshow("input", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
