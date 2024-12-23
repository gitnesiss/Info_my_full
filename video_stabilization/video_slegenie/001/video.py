# Первая программа находит точки интереса
# Вторая программа просто открывает картинки в своих окнах

import cv2
# Загрузка изображения
# image = cv2.imread("2024-05-30_123026.png", -1)
image = cv2.imread('C:\\code\\Info_my_full\\video_stabilization\\video_slegenie\\002_find_object\\images\\scale_2400.png', 1)
# Создание объекта детектора ORB
orb = cv2.ORB_create()
# Поиск ключевых точек и их описаний на изображении
keypoints, descriptors = orb.detectAndCompute(image, None)
# Рисование найденных ключевых точек на изображении
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)
# image_with_keypoints = cv2.drawKeypoints(image, keypoints, 0, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# Вывод изображения с ключевыми точками
cv2.imshow('Image with Keypoints', image_with_keypoints)  # Вывод изображения с ключевыми точками
# cv2.imshow('Image with Keypoints', image)  # Вывод оригинального изображения
cv2.waitKey(0)  
cv2.destroyAllWindows()





import cv2
import numpy as np
# img = cv2.imread("py_logo.png")
img = cv2.imread('C:\\code\\Info_my_full\\video_stabilization\\video_slegenie\\002_find_object\\images\\2024-05-30_123026.png', 1)
cv2.namedWindow("image_logo", cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow("image_logo", cv2.WINDOW_NORMAL)
cv2.imshow("image_logo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('C:\\code\\Info_my_full\\video_stabilization\\video_slegenie\\002_find_object\\images\\py_logo.png', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()