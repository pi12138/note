'''
识别照片中特定的面部特征
并且在面部特征处划线
'''

import face_recognition
from PIL import Image,ImageDraw

image1 = face_recognition.load_image_file('./unknow/1.jpg')
# print(image1)
# 返回列表，列表内容为面部特征字典
face_landmarks_list = face_recognition.face_landmarks(image1)
# print("There are {} people.".format(len(face_landmarks)))
# for k,v in face_landmarks.items():
    # print(k,':',v)

pil_image = Image.fromarray(image1)
# print(pil_image)
# pil_image.show()
d = ImageDraw.Draw(pil_image)
# print(d)
for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        print("{0}:{1}".format(facial_feature, face_landmarks[facial_feature]))
    
    for facial_feature in face_landmarks.keys():
        # 画一条线，或一系列连接的线段。
        d.line(face_landmarks[facial_feature], width=5)

# 显示图片
pil_image.show()

