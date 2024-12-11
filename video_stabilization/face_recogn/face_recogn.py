# Распознование лиц по видеокамере.

import cv2

# создаём переменную с файлом модели
face_cascade = cv2.CascadeClassifier('/home/roman/code/python/py_prj/prj_005_face_recogn/haarcascade_frontalface_default.xml')

# читаем изображение
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(0)

    # обесцвечиваем изображение
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # находим лица на обесцвеченном изображении
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # на цветном изображении рисуем квадраты там, где нашли лица на обесцвеченном
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # открываем изображение в отдельном окне

    cv2.imshow('image', frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()