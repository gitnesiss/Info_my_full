# import required libraries
from vidgear.gears import CamGear
import cv2

# Open any source of your choice, like Webcam first index(i.e. 0)
# and change its colorspace to `HSV`
stream = CamGear(source=0, colorspace="COLOR_BGR2HSV", logging=True).start()

text="change colors: a, s, d, f"
text2="exit: q"

# loop over
while True:

    # read HSV frames
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}
    cv2.putText(frame, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, text2, (5, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) 

    # Show output window
    cv2.imshow("Output", frame)

    # check for key if pressed
    key = cv2.waitKey(1) & 0xFF

    # check if 'w' key is pressed
    if key == ord("a"):
        # directly change colorspace at any instant
        stream.color_space = cv2.COLOR_BGR2GRAY  # Now colorspace is GRAY

    # check for 'e' key is pressed
    if key == ord("s"):
        stream.color_space = cv2.COLOR_BGR2LAB  # Now colorspace is CieLAB

    if key == ord("d"):
        # directly change colorspace at any instant
        stream.color_space = cv2.COLOR_BGR2HSV  # Now colorspace is HSV

    # check for 's' key is pressed
    if key == ord("f"):
        stream.color_space = None  # Now colorspace is default(ie BGR)

    # check for 'q' key is pressed
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()