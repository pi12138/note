'''
使用网络摄像头识别实时视频中的人脸-简单/慢版本(需要安装OpenCV)
'''

import face_recognition
import cv2

image_xyjy = face_recognition.load_image_file('./know/xyjy.jpg')
image_sylm = face_recognition.load_image_file('./know/sylm.jpg')
# print(type(image_sylm))   # <class 'numpy.ndarray'>

xyjy_face_encodings = face_recognition.face_encodings(image_xyjy)[0]
sylm_face_encodings = face_recognition.face_encodings(image_sylm)[0]

know_face_encodings = [xyjy_face_encodings, sylm_face_encodings]
know_face_name = ['xyjy', 'sylm']

capture = cv2.VideoCapture(0)

while True:
    ret,frame = capture.read()
    # print(type(frame))    # <class 'numpy.ndarray'>
    rgb_frame = frame[:,:,::-1]
    # print(type(rgb_frame))    # <class 'numpy.ndarray'>
    face_locations = face_recognition.face_locations(rgb_frame)
    video_face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    # print(len(video_face_encodings))
    # print(video_face_encodings)
    for (top,right,bottom,left), face_encoding in zip(face_locations,  video_face_encodings):
        matches = face_recognition.compare_faces(know_face_encodings, face_encoding)
        # print(matches)
        name = 'unknown'

        if True in matches:
            first_match_index = matches.index(True)
            name = know_face_name[first_match_index]

        cv2.rectangle(frame, (left,top), (right,bottom), (0,0,255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ('q'):
            break
    
capture.release()
cv2.destroyAllWindows()


