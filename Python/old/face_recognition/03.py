'''
自动找到图像中的所有面孔
GPU加速
不能运行？？？
'''

from PIL import Image
import face_recognition

#加载图片
image1 = face_recognition.load_image_file('./unknow/1.jpg')

# 返回一个列表，列表中用元组保存图片中的所有人脸的位置
# face_locations = face_recognition.face_locations(image1)
face_locations = face_recognition.face_locations(image1,number_of_times_to_upsample=0,model='cnn')
# print(face_locations)
print("There are {} people in the picture.".format(len(face_locations)))

for face_location in face_locations:
    # 元组中图片坐标为上，右，下，左
    top,right,bottom,left = face_location

    face_image = image1[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()