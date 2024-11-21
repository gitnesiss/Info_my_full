# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
from vidgear.gears import VideoGear
import numpy as np
import cv2
import datetime

# open any valid video stream with stabilization enabled(`stabilize = True`)
stream_stab = VideoGear(source=0, stabilize=True).start()

# Define WriteGear Object with suitable output filename for e.g. `Output.mp4`
writer = WriteGear(output = 'Stab_video.mp4') 

# loop over
while True:
    # read stabilized frames
    frame_stab = stream_stab.read()

    # check for stabilized frame if None-type
    if frame_stab is None:
        break

    # {do something with the frame here}

    # добавляю слой для возможности вставить текст. Если этого не сделать программа не будет работать
    image = np.ascontiguousarray(frame_stab, dtype=np.uint8)

    # Вывод времени и даты на фрейм
    # Русский стиль
    date="Time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %a"))
    # Американский стиль
    # date="Time: {}".format(datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p"))
    # Вывожу в консоль дату и время
    print(date)
    # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
    cv2.putText(image, date, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 50), 1) 

    # Куда вставлять, что написать, начало координат расположения текста, шрифт, масштаб шрифта, цвет, толщина)
    cv2.putText(image, "Stibilaze: on", (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2,)

    # Запись кадра в файл
    writer.write(image)

    # Show output window
    cv2.imshow("Stabilized Output", image)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close streams
stream_stab.stop()