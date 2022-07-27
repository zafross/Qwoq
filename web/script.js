

let btn = document.querySelector("#submit");
btn.addEventListener("click", sendData);

let btn2 = document.querySelector("#cancel");
btn2.addEventListener("click", Cancel);

async function Cancel() {
	// Hide page 2 and shows page 1 (where the start button is)
	document.querySelector(".Second_screen").style.display='none';
	document.querySelector(".First_screen").style.display='block';
	await eel.cancel();
}

async function sendData() {
	let r_id = document.querySelector('#reddit').value;
	let channel_id = document.querySelector('#channel_id').value;
	let amount = document.querySelector('#amount').value;
	document.querySelector(".First_screen").style.display='none';
	document.querySelector(".Second_screen").style.display='block';
	// Hide page 1 and shows page 2 (where the stop button is)
	// and send inputed data to python
	await eel.get_data(r_id, channel_id, amount);
}

eel.expose(set_progres)
function set_progres(pixel) {
	// progress bar
	document.querySelector("#load").style.width = pixel;
}



eel.expose(set_params)
function set_params(r_id, channel_id) {
	// last inputed params
	document.querySelector("#channel_id").value = channel_id;
	document.querySelector("#reddit").value = r_id;
}

async function Loaded_js() {
	await eel.on_load_js();
}
Loaded_js()
