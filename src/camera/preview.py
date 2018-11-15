import picamera
import time


# documentaion
url = "https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.start_preview"
url = "https://projects.raspberrypi.org/en/projects/getting-started-with-picamera"

# start and stop previewing
camera = picamera.PiCamera()
camera.start_preview()
time.sleep(10)
camera.stop_preview()