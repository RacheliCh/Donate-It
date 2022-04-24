from picamera import PiCamera
from time import sleep
from firebase_storage import *
from firebase_firestore import *

camera = PiCamera()
storageInitialize()
firestoreInitialize()

print("pushed")
now = datetime.now()
dt = now.strftime("%d%m%Y%H:%M:%S")
img_name = dt + ".jpg"
camera.capture(img_name)
print(img_name+" saved")

storageUploadImage(img_name)

print("Image sent")
os.remove(img_name)
print("File Removed")

img_url = storageGetImageUrl(img_name)

data = {
    'type': 'skirt',
    'size': 's',
    'image': img_url
}

firestoreAddDocument(data)


camera.close()