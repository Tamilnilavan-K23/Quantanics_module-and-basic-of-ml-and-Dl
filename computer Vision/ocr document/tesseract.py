import pytesseract as tess
#tess.pytesseract.tesseract_cmd=r'F:\quantanics\library needed\tesseract.exe'
from PIL import Image


img=Image.open('F:\quantanics\computer Vision\ocr document\image.png')
text=tess.image_to_string((img))
print(text)



























