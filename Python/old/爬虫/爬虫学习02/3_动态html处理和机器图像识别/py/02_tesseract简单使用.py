from pytesseract import image_to_string
from PIL import Image


image = Image.open('../image/zm.png')

text = image_to_string(image)

print("图片里的文字为：{}".format(text))