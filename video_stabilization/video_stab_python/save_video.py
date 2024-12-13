# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2
import datetime

# Open suitable video stream, such as webcam on first index(i.e. 0)
stream = CamGear(source=0).start() 

# Define WriteGear Object with suitable output filename for e.g. `Output.mp4`
writer = WriteGear(output = 'Output_2.mp4') 

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if None-type
    if frame is None:
        break


    # {do something with the frame here}

    # Вывод времени и даты на фрейм
    # Русский стиль
    date="Time: {}".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %a"))
    # Американский стиль
    # date="Time: {}".format(datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p"))
    print(date)
    cv2.putText(frame, date, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2) 

    # Запись кадра в файл
    writer.write(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()



