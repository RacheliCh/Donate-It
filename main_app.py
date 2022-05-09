from picamera import PiCamera
from time import sleep
from firebase_storage import *
from firebase_firestore import *

camera = PiCamera()
camera.framerate=30
camera.resolution=(1080,1080)
camera.start_preview()
sleep(5)
camera.stop_preview()

storageInitialize()
firestoreInitialize()

print("pushed")
now = datetime.now()
dt = now.strftime("%d%m%y%H%M%S")
img_name = dt + ".jpg"
camera.capture(img_name)
print(img_name+" saved")

storageUploadImage(img_name)

print("Image sent")
os.remove(img_name)
print("File Removed")

img_url = storageGetImageUrl(img_name)

data = {
    'type': 'shorts',
    'size': 'M',
    'color': 'red',
    'price': '20',
    'image': img_url
}

firestoreAddDocument(data, dt)

camera.close()

print("done")