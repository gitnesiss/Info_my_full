# https://github.com/abhiTronix/vidgear/wiki/Real-time-Video-Stabilization#real-time-video-stabilization-with-vidgear

# https://abhitronix.github.io/vidgear/latest/

# import libraries
from vidgear.gears import VideoGear
from vidgear.gears import WriteGear
import cv2

stream = VideoGear(source=0, stabilize = True).start() # To open any valid video stream(for e.g device at 0 index)

# infinite loop
while True:

    frame = stream.read()
    # read stabilized frames

    # check if frame is None
    if frame is None:
        #if True break the infinite loop
        break

    # do something with stabilized frame here

    cv2.imshow("Stabilized Frame", frame)
    # Show output window

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        #if 'q' key-pressed break out
        break

cv2.destroyAllWindows()
# close output window

stream.stop()
# safely close video stream



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
