import face_recognition
from PIL import Image

# image = face_recognition.load_image_file("C:\code\python\\1.jpg")
# face_locations = face_recognition.face_locations(image)

picture_of_me = face_recognition.load_image_file("C:\code\python\\3.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

unknown_picture = face_recognition.load_image_file("C:\code\python\\2.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("Найден!")
else:
    print("Кто то другой!")

# for face_location in face_locations:
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
#     face_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(face_image)
#     pil_image.show()