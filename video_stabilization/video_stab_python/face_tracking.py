import cv2
import numpy as np
from cffi import FFI



def box():
    ffi=FFI() 
    ffi.cdef("""
            int MessageBoxA(HWND hWnd, LPCSTR lpText, LPCSTR lpCation, UINT uType);
            """)
    _user32 = ffi.dlopen("USER32.DLL")
    lpText = bytes("Hello from cffi", "utf-8")
    lpCaption = bytes("Test cffi", "utf-8")
    MB_OK = 1
    if _user32.MessageBoxA(ffi.NULL, lpText, lpCaption, MB_OK):
        print("MessageBox showed!")



# https://www.youtube.com/watch?v=AmnWuw3z9jA

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, frame = cap.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обвести лицо зелёным прямоугольником
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for (x, y , w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Обвести глаза синим прямоуглоьником
        # Создаём доплнительную переменную куда записываем координаты лица и в этой области будем искать глаза
        img_gray_face = img_gray[y:y+h, x:x+w]
        eyes = eye_cascade_db.detectMultiScale(img_gray_face, 1.1, 19)
        for (ex, ey , ew, eh) in eyes:
            cv2.rectangle(frame, (x+ex, y+ey), (x + (ex + ew), y + (ey + eh)), (255, 0, 0), 2)

    cv2.imshow("Output", frame)
    # Выход через клавишу 'q'
#    if cv2.waitKey(1) & 0xFF == ord('q'):
    # Выход через клавишу 'esc'
    if cv2.waitKey(1) & 0xFF == 27: 
        break

# Освобождаем доступ к камере
cap.release()
cv2.destroyAllWindows()