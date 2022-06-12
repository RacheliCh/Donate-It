import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def firestoreInitialize():
    global db
    cred = firebase_admin.credentials.Certificate("/home/pi/Documents/project/Donate-It/rpi/DonateItServiceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

def firestoreAddDocument(doc, doc_id):
    db.collection('items').document(doc_id).set(doc)