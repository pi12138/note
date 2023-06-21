from PIL import Image
import pytesseract

# 生成一个图片实例
image = Image.open('./验证码图片/9.jpg')

# 使用pytesseract将图片转为文字
# 返回结果就是转换后的结果
text = pytesseract.image_to_string(image)
print(type(text))
print(text)