'''
应用（可怕的丑陋）数字化妆
不忍直视
'''

from PIL import Image,ImageDraw
import face_recognition

image1 = face_recognition.load_image_file('./know/xyjy.jpg')

face_landmarks_list = face_recognition.face_landmarks(image1)

for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(image1)
    # pil_image.show()
    d = ImageDraw.Draw(pil_image)

    # fill参数用于填充颜色
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    # d.polygon(face_landmarks['left_eyebrow'], fill='blue')
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)
    # pil_image.show()

    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Sparkle the eyes
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)
    
    pil_image.show()
