import pytesseract
from PIL import Image

result = pytesseract.image_to_string(Image.open('D:/qn200416174112d49d8d1cfe03676aad188b2be1136a43.jpg'))
print(result)
