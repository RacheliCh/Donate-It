import { syncData } from "backend/firebaseModule.jsw";
import wixData from "wix-data"

$w.onReady(function () {
    doSync();
});

const doSync = async () => {
    await syncData();  
    $w('#dataset1').refresh();
}

// Filters items in gallery by input
function filter(title){
    $w('#dataset1').setFilter(wixData.filter().contains("search_info", title));
}
export function search_item_click(event, $w) { 
    filter($w('#input1').value);
}

// When moving between gallery pages - will jump to the top of the page
export function pagination1_click(event) {
    $w('#anchor1').scrollTo();
}

// When there is no input for search - will show all items
export function input1_input(event) {
    if($w('#input1').value == ""){
        $w('#dataset1').setFilter(wixData.filter());
    }
}
