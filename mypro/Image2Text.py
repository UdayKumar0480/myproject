
import pytesseract
#import Image
from PIL import Image

pytesseract.pytesseract.tesseract_cmd= (r"C:\Python37\Scripts\pytesseract.exe")
#pytesseract.pytesseract.tesseract_cmd= (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
img = Image.open(r"D:\file.jpg")
text=pytesseract.image_to_string(img)
print(text)
'''



from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (r"C:\Python37\Scripts\pytesseract.exe")

img = (r"D:\download.jpg")

print(pytesseract.image_to_string(Image.open(img)))
'''