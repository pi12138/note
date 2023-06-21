'''
在图像中识别人脸，识别他们是谁
'''

import face_recognition
# 读取图片
xyjy_image = face_recognition.load_image_file('./know/xyjy.jpg')
sylm_image = face_recognition.load_image_file('./know/sylm.jpg')
qzx_image = face_recognition.load_image_file('./know/qzx.jpg')
unknow_image = face_recognition.load_image_file('./unknow/1.jpg')
# 读取图片中人脸面部编码
xyjy_face_encodings = face_recognition.face_encodings(xyjy_image)[0]
sylm_face_encodings = face_recognition.face_encodings(sylm_image)[0]
qzx_face_encodings = face_recognition.face_encodings(qzx_image)[0]
unknow_face_encodings = face_recognition.face_encodings(unknow_image)[0]

face_encodings = [xyjy_face_encodings, sylm_face_encodings, qzx_face_encodings]
# for i in face_encodings:
    # print(i)
# 将面部编码列表和候选编码对比，返回对比结果值为bool类型的列表
result = face_recognition.compare_faces(face_encodings, unknow_face_encodings, tolerance=0.4)

# print(result)
if result[0] == True:
    print("she is xyjy.")
elif result[1] == True:
    print('she is sylm.')
elif result[2] == True:
    print("she is qzx.")
else:
    print("who does she?")

