import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'# Download tesseract from internet
from PIL import Image
img=Image.open('OCR.jpg')
text=tess.image_to_string((img))
print(text)
