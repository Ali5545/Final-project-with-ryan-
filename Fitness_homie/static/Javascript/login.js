window.addEventListener("load", click); 

function click()
{
	document.getElementById("submit").addEventListener("click", check); 
}
function check() 
{
	let username = document.getElementById("username").value; 
	let pass = document.getElementById("password").value; 
	
	switch(true)
	{
		case username == "":
			document.getElementById("username").focus();
			alert("There is missing information"); 
			break; 
		case pass == "":
			document.getElementById("password").focus(); 
			alert("There is missing information"); 
			break; 
		default: 
			break; 
	}
}
			
