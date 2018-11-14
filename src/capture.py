import picamera


# documentaion
url = "https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.capture"
extensions = [
    'jpeg',
    'png',
    'gif',
    'bmp',
    'yuv',
    'rgb',
    'rgba',
    'bgr',
    'bgra'
    ]

# name & extension
name = "example"
extension = extensions[0]
image = '{}.{}'.format(name, extension)

# capture an image
camera = picamera.PiCamera()
camera.capture(image)
