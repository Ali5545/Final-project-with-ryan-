window.addEventListener("load", click); 

function click()
{
	document.getElementById("submit").addEventListener("click", check); 
}
function check() 
{
	let username = document.getElementById("username").value; 
	let pass = document.getElementById("password").value; 
	let email = document.getElementById("email").value; 
	
	let check1 = pass.length; 
	let check2 = email/1; 
	let check3 = parseInt(email)/1; 
	
	switch(true)
	{
		case username == "" || pass == "" || email == "":
			document.getElementById("username").focus();
			alert("There is missing information"); 
			break; 
		case check1 < 6:
			document.getElementById("password").focus(); 
			alert("You have to input a password that is at least 6 characters long!"); 
			break; 
		case check2 == check3: 
			document.getElementById("username").focus(); 
			alert("You have to cannot input a email that is just numbers");
			break;
		default: 
			break; 
	}
}