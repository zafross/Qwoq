

let btn = document.querySelector("#submit");
btn.addEventListener("click", sendData);

let btn2 = document.querySelector("#cancel");
btn2.addEventListener("click", Cancel);

async function Cancel() {
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
	await eel.get_data(r_id, channel_id, amount);
}

eel.expose(set_progres)
function set_progres(pixel) {
	console.log(pixel)
	document.querySelector("#load").style.width = pixel;
}

