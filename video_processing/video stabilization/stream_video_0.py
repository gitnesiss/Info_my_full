# import required libraries
from vidgear.gears import CamGear
import cv2

# set desired quality as 720p
# options = {"STREAM_RESOLUTION": "720p"}

# Add any desire Video URL as input source
# for e.g https://vimeo.com/151666798
# and enable Stream Mode (`stream_mode = True`)
stream = CamGear(
    source='rtsp://admin:123456@192.168.11.174:554/stream0',
    stream_mode=False,
    logging=True,
    # **options
).start()

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # Show output window
    cv2.imshow("Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()