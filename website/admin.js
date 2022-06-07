import { removeItem, syncData} from "backend/firebaseModule.jsw";

const doSync = async () => {
    await syncData();
}

// Shows remove button only if there is input in the box
export function inputRemove_input(event) {
	$w('#buttonRemove').show();

	if ($w('#inputRemove').value === "") {
		$w('#buttonRemove').hide();
	}
}

// When Remove button is clicked:
// If item is in database - will remove from firestore and show Success message
// If item is not in database - show Error message
export function buttonRemove_click(event) {
	const item_id_to_remove = $w('#inputRemove').value;

	removeItem(item_id_to_remove).then(
		function(value) {
			$w('#SuccessText').show();
			$w('#inputRemove').value="";
			setTimeout(() => { $w("#SuccessText").hide(); }, 2000);
			doSync();
		},

		function(error) {
			$w('#idnotfoundText').show();
			$w('#inputRemove').value="";
			setTimeout(() => { $w("#idnotfoundText").hide(); }, 2000);
		}
	);
}
