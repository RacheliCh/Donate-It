/*********
 .jsw file

**********/

// code in backend/firebaseModule.jsw

import { initializeApp } from 'firebase/app';
import { getFirestore, collection, getDocs, doc, deleteDoc } from 'firebase/firestore/lite';
import { getStorage, ref, deleteObject } from "firebase/storage";
import wixData from 'wix-data';

const firebaseConfig = {
    apiKey: "AIzaSyBfYHarCf_LRBBrQSUCzIlO9PEVj8oGQRE",
    authDomain: "donateit-d274f.firebaseapp.com",
    projectId: "donateit-d274f",
    storageBucket: "donateit-d274f.appspot.com",
    messagingSenderId: "508136337397",
    appId: "1:508136337397:web:98fb282ad141c254b03abc",
    measurementId: "G-BGC246215Q"
};

const app = initializeApp(firebaseConfig);

const db = getFirestore(app);

const storage = getStorage();

let allImageIds = []; // array of picture-ids thats in firestore db = the ground truth

// Sync data between firebase and WIX db
export async function syncData() {
    const snapshot = await getDocs(collection(db, 'items')); // gets all items in firebase db, each is a doc
    const docArray = []; // array of promises, needed for wix stuff
    snapshot.forEach((doc) => { 
        docArray.push(doc);
    });

    allImageIds = docArray.map(doc => doc.id); // array of picture-ids thats in firestore db = the ground truth

    // adding products
    const {items: products} = await wixData.query("products").limit(1000).find(); // finds items in wix db
    const docsToAdd = docArray.filter(doc => !products.some(product => product._id === doc.id)).map(doc => ( // filters items in firebase db that are not in wix db. these are the items that we want to add to wix db
       doc.data()
    ));
    await Promise.all(docsToAdd.map(doc => wixData.insert("products", doc, { suppressAuth: true })));
    
    // removing products
    const productsToDelete = products.filter(product => !allImageIds.includes(product._id)); // filters products in wix db that are not in firebase db. these are the products that we want to erase from wix db
    await Promise.all(productsToDelete.map(product => wixData.remove("products", product._id, { suppressAuth: true })));

}

// Remove procuct by id
export async function removeItem(item_id_to_remove) {
    const prodToRemove = allImageIds.filter(( product => product === item_id_to_remove));

    if (prodToRemove.length === 0){ // product was not found in firebase. nothing to be done
        throw new Error("Whoops!");
    }
    else{  // product was found in firebase. need to erase from firestore and storage dbs
        await deleteDoc(doc(db, 'items', item_id_to_remove));

        // Create a reference to the file to delete
        const desertRef = ref(storage, item_id_to_remove + '.jpg');
        // Delete the file
        await deleteObject(desertRef).then(() => {
            // File deleted successfully
        }).catch((err) => {
            let errorMsg = err;
            console.log(errorMsg);
        });

        return 0;
    }
}