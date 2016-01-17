import numpy as np
import cv2

if __name__ == "__main__":
    print "Press ESC to exit ..."

# create windows
cv.NamedWindow('Raw', cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('Processed', cv.CV_WINDOW_AUTOSIZE)

# create capture device
device = 0 # assume we want first device
capture = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)


# check if capture device is OK
if not capture:
    print "Error opening capture device"
    sys.exit(1)

while 1:
    # do forever

    # capture the current frame
    frame = cv.QueryFrame(capture)
    if frame is None:
        break

    # mirror
    cv.Flip(frame, None, 1)

    # face detection
    detect(frame)

    # display webcam image
    cv.ShowImage('Raw', frame)

    # handle events
    k = cv.WaitKey(10)

    if k == 0x1b: # ESC
        print 'ESC pressed. Exiting ...'
        break

    if k == 0x63 or k == 0x43:
        print 'capturing!'
        cv.SaveImage("test.jpg",frame) 