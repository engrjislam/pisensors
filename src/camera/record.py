import picamera
import time


# documentaion
url = "https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.start_recording"
extensions = [
    'h264',
    'mjpeg',
    'yuv',
    'rgb',
    'rgba',
    'bgr',
    'bgra'
    ]

# name & extension
name = "examplevid"
extension = extensions[0]
video = '{}.{}'.format(name, extension)

# start and stop recording
camera = picamera.PiCamera()
camera.start_recording(video)
time.sleep(5)
camera.stop_recording()
