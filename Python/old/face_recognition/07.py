'''
对比人脸差别
'''

import face_recognition

xyjy_image = face_recognition.load_image_file('./know/xyjy.jpg')
sylm_image = face_recognition.load_image_file('./know/sylm.jpg')
zyw_image = face_recognition.load_image_file('./know/zyw.jpg')

xyjy_face_encodings = face_recognition.face_encodings(xyjy_image)[0]
sylm_face_encodings = face_recognition.face_encodings(sylm_image)[0]
zyw_face_encodings = face_recognition.face_encodings(zyw_image)[0]

know_face_encodings = [xyjy_face_encodings, sylm_face_encodings, zyw_face_encodings]

unknow_image = face_recognition.load_image_file('./unknow/1.jpg')
unknow_face_encodings = face_recognition.face_encodings(unknow_image)[0]

distance = face_recognition.face_distance(know_face_encodings, unknow_face_encodings)

print(distance)

for i, face_distance in enumerate(distance):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()
