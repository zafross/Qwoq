var btn_image = 1
var btn_copyright = 1

let btn = document.querySelector("#submit");
btn.addEventListener("click", sendData);

document.querySelector("#amount_plus_png").addEventListener("click", function() {
	document.querySelector("#amount").value = parseInt(document.querySelector("#amount").value) + 1
});
document.querySelector("#amount_minus_png").addEventListener("click", function() {
	document.querySelector("#amount").value = parseInt(document.querySelector("#amount").value) - 1
});
document.querySelector("#amount_plus").addEventListener("click", function() {
	document.querySelector("#amount").value = parseInt(document.querySelector("#amount").value) + 1
});
document.querySelector("#amount_minus").addEventListener("click", function() {
	document.querySelector("#amount").value = parseInt(document.querySelector("#amount").value) - 1
});


document.querySelector("#cooldown_plus_png").addEventListener("click", function() {
	document.querySelector("#cooldown").value = parseInt(document.querySelector("#cooldown").value) + 1
});
document.querySelector("#cooldown_minus_png").addEventListener("click", function() {
	document.querySelector("#cooldown").value = parseInt(document.querySelector("#cooldown").value) - 1
});
document.querySelector("#cooldown_plus").addEventListener("click", function() {
	document.querySelector("#cooldown").value = parseInt(document.querySelector("#cooldown").value) + 1
});
document.querySelector("#cooldown_minus").addEventListener("click", function() {
	document.querySelector("#cooldown").value = parseInt(document.querySelector("#cooldown").value) - 1
});

let btn3 = document.querySelector("#image");
btn3.addEventListener("click", function() {
	if (btn_image == 1) {
		btn3.style.background = 'rgba(255, 0, 0, 0.26)';
		btn3.textContent = 'No'
		btn_image = 0
	}
	else {
		btn3.style.background = 'rgba(70, 233, 56, 0.18)';
		btn3.textContent = 'Yes'
		btn_image = 1
	};
});

let btn4 = document.querySelector("#copyright");
btn4.addEventListener("click", function() {
	if (btn_copyright == 1) {
		btn4.style.background = 'rgba(255, 0, 0, 0.26)';
		btn4.textContent = 'No'
		btn_copyright = 0
	}
	else {
		btn4.style.background = 'rgba(70, 233, 56, 0.18)';
		btn4.textContent = 'Yes'
		btn_copyright = 1
	};
});

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
	let cooldown = document.querySelector('#cooldown').value;
	let token = document.querySelector('#token').value;

	// document.querySelector(".First_screen").style.display='none';
	// document.querySelector(".Second_screen").style.display='block';
	// Hide page 1 and shows page 2 (where the stop button is)
	// and send inputed data to python 

	// r_id, channel_id, amount, token, image, copyright, cooldown=1000
	await eel.get_data(r_id, channel_id, amount, token, btn_image, btn_copyright, cooldown);
}

eel.expose(set_progres)
function set_progres(pixel) {
	// progress bar
	document.querySelector("#load").style.width = pixel;
}



eel.expose(set_params)
function set_params(r_id, channel_id, token, amount, cooldown, image, copyright) {
	// last inputed params
	document.querySelector("#channel_id").value = channel_id;
	document.querySelector("#reddit").value = r_id;
	document.querySelector("#token").value = token;
	document.querySelector("#amount").value = amount;
	document.querySelector("#cooldown").value = cooldown;
	if(image == '0') {
		btn3.style.background = 'rgba(255, 0, 0, 0.26)';
		btn4.textContent = 'No'
		btn_image = 0
	};
	if(copyright == '0') {
		btn4.style.background = 'rgba(255, 0, 0, 0.26)';
		btn4.textContent = 'No'
		btn_copyright = 0
	};
}

async function Loaded_js() {
	await eel.on_load_js();
}
Loaded_js()
