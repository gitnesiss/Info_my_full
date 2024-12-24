# https://github.com/abhiTronix/vidgear/wiki/Real-time-Video-Stabilization#real-time-video-stabilization-with-vidgear

# https://abhitronix.github.io/vidgear/latest/

# import libraries
from vidgear.gears import VideoGear
from vidgear.gears import WriteGear
import cv2

# Открыть любой допустимый видеопоток (например, для устройства с индексом 0)
stream = VideoGear(source=0, stabilize = True).start()

# Бесконечный цикл
while True:

    # читать стабилизированные кадры
    frame = stream.read()

    # проверка, отсутствует ли кадр
    if frame is None:
        # если True, прервать бесконечный цикл
        break

    # Здесь можно что-нибудь сделать со стабилизированным кадром

    # Показать окно вывода
    cv2.imshow("Stabilized Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # проверка нажатия клавиши «q»
    if key == ord("q"):
        # если клавиша 'q' нажата, выйти из бесконечного цикла
        break

# закрыть окно вывода
cv2.destroyAllWindows()

# безопасно закрыть видеопоток
stream.stop()



# Я немного опоздал, но я создал мощную и многопоточную 
# библиотеку VidGear Video Processing на Python, которая 
# теперь обеспечивает стабилизацию видео в реальном 
# времени с минимальной задержкой и за счет незначительного 
# или нулевого дополнительного требования к вычислительной 
# мощности с Stabilizer Class . Основная идея заключается 
# в отслеживании и сохранении массива основных признаков 
# для заданного количества кадров, а затем использовании 
# этих опорных точек для отмены всех возмущений относительно 
# него для входящих кадров в очереди. Вот простой пример 
# использования для вашего удобства:

# https://answers.opencv.org/question/6843/realtime-video-stabilization/
