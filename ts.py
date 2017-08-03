try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

print (pytesseract.image_to_string(Image.open("1.png")))
print (pytesseract.image_to_string(Image.open('2.png'), lang='eng'))
print (pytesseract.image_to_string(Image.open('3.png'), lang='eng'))