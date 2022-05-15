from firebase_storage import *
from firebase_firestore import *
from system import *

# initialize software component
set_system_time()
storageInitialize()
firestoreInitialize()
my_camera = cameraInitialize()

id, img_url = takePictureAndUpload(my_camera)

data = {
    'type': 'shorts',
    'size': 'M',
    'color': 'red',
    'price': '20',
    'image': img_url
}

firestoreAddDocument(data, id)

my_camera.close()

print("done")