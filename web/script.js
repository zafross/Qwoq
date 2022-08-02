var btn_image = 1
var btn_copyright = 1                /*Project created with love by zafros*/
var cancel_status = 0

document.querySelector("#submit").addEventListener("click", sendData);
document.querySelector("#back").addEventListener("click", Cancel);

document.querySelector("#notify_ok").addEventListener("click", function() {
	document.querySelector(".notify").style.opacity ='0';
	document.querySelector("#blur").style.opacity ='0';
	setTimeout(function(){
		document.querySelector("#blur").style.display='none';
		document.querySelector(".notify").style.display='none';
	}, 150)
	
});

document.querySelector("#background_card_me").addEventListener("click", function() {
	window.open("https://github.com/zafross");
});
document.querySelector("#background_card_star").addEventListener("click", function() {
	window.open("https://github.com/zafross/Qwoq");
});
document.querySelector("#version").addEventListener("click", function() {
	window.open("https://github.com/zafross/Qwoq");
});
document.querySelector("#logo").addEventListener("click", function() {
	window.open("https://github.com/zafross/Qwoq");
});

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
	document.querySelector("#cooldown").value = parseInt(document.querySelector("#cooldown").value) + 100
});
document.querySelector("#cooldown_minus_png").addEventListener("click", function() {
	document.querySelector("#cooldown").value = parseInt(document.querySelector("#cooldown").value) - 100
});
document.querySelector("#cooldown_plus").addEventListener("click", function() {
	document.querySelector("#cooldown").value = parseInt(document.querySelector("#cooldown").value) + 100
});
document.querySelector("#cooldown_minus").addEventListener("click", function() {
	document.querySelector("#cooldown").value = parseInt(document.querySelector("#cooldown").value) - 100
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
		btn4.textContent = 'No';
		btn_copyright = 0;
	}
	else {
		btn4.style.background = 'rgba(70, 233, 56, 0.18)';
		btn4.textContent = 'Yes';
		btn_copyright = 1;
	};
});

eel.expose(Done)
function Done(amount) {
	document.querySelector("#loading").style.background = '#E9D312';
	document.querySelector("#loading").style.boxShadow = '0px 0px 15px rgba(255, 230, 0, 0.35)';
	document.querySelector("#title_process").textContent = 'Process completed successfully!';
	document.querySelector("#done_title").style.opacity = '1';
	document.querySelector("#counter").textContent = amount + '/' + amount;
	document.querySelector("#loading").style.width = '742px';
}

eel.expose(Cancel)
function Cancel() {
	// Hide page 2 and shows page 1 (where the start button is)
	document.querySelector(".Second_screen").style.display='none';
	document.querySelector(".First_screen").style.display='block';
	document.querySelector("#loading").style.background = 'rgba(132, 36, 255, 0.51)';
	document.querySelector("#loading").style.boxShadow = '0px 0px 20px rgba(158, 0, 255, 0.1)';
	document.querySelector("#title_process").textContent = 'Process started';
	document.querySelector("#done_title").style.opacity = '0';
	document.querySelector("#loading").style.width = '10px';
	document.querySelector("#loading").style.opacity = '0';
	cancel_status = 1;
}

/*Project created with love by zafros*/
async function sendData() {
	let r_id = document.querySelector('#reddit').value;
	let channel_id = document.querySelector('#channel_id').value;
	let amount = document.querySelector('#amount').value;
	let cooldown = document.querySelector('#cooldown').value;
	let token = document.querySelector('#token').value;

	if(r_id != '' && channel_id != '' && amount != '' && token != '') {
		if(amount > 0 && cooldown >= 0) {
			document.querySelector(".First_screen").style.display='none';
			document.querySelector(".Second_screen").style.display='block';
			document.querySelector("#counter").textContent = '0/'+amount;
			// Hide page 1 and shows page 2 (where the stop button is)
			// and send inputed data to python 

			// r_id, channel_id, amount, token, image, copyright, cooldown=1000
			await eel.get_data(r_id, channel_id, amount, token, btn_image, btn_copyright, cooldown);	
		}
		else {
			notify('Invalid amount or cooldown', 'Both fields must be greater than or equal to 0. Click on the version to read the documentation.')
		};
			
	}
	else {
		notify('Please fill in all fields.', "If you don't know what to put in a field, click on the version and read the documentation.")
	}
}

eel.expose(give_cancel_status)
function give_cancel_status() {
	if (cancel_status == 1) {
		document.querySelector("#loading").style.background = 'rgba(132, 36, 255, 0.51)';
		document.querySelector("#loading").style.boxShadow = '0px 0px 20px rgba(158, 0, 255, 0.1)';
		document.querySelector("#title_process").textContent = 'Process started';
		document.querySelector("#done_title").style.opacity = '0';
		document.querySelector("#loading").style.width = '10px';
		document.querySelector("#loading").style.opacity = '0';
		cancel_status = 0
		return 1;
	}
	else {
		return 0;
	}
}

eel.expose(set_progres)
function set_progres(pixel, txt) {
	// progress bar
	document.querySelector("#loading").style.opacity = '1';
	document.querySelector("#loading").style.width = pixel;
	document.querySelector("#counter").textContent = txt;
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

eel.expose(notify)
function notify(title, subtitle) {
	document.querySelector("#blur").style.display='block';
	document.querySelector(".notify").style.display='block';
	setTimeout(function(){
		document.querySelector("#blur").style.opacity ='1';
		document.querySelector(".notify").style.opacity ='1';
	}, 150)

	document.querySelector("#notify_title").textContent = title
	document.querySelector("#notify_subtitle").textContent = subtitle
}
