'''
使用face_recognition
'''

import face_recognition
import cv2

image = cv2.imread('2.jpg')
# image = face_recognition.load_image_file('2.jpg')
# face_locations = face_recognition.face_locations(image)


print(type(image))
print(image)

# print(type(face_locations))
# print(face_locations)
cv2.imshow('xyjy', image)
# cv2.imshow('xyjy', face_locations)

cv2.waitKey(0)

cv2.destroyAllWindows()
