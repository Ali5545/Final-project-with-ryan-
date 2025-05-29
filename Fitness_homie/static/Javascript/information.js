window.addEventListener("load", addlistener);


function addlistener()
{
	document.getElementById("submit").addEventListener("click",check);
}
function check()
{
	let age = document.getElementById("age");
	let feet = document.getElementById("Feet");
	let inches = document.getElementById("Inches");
	let weight = document.getElementById("weight");

	switch(true)
	{
		case feet == "":
			document.getElementById("age").focus(); 
			alert("You must type something into all of the input boxes!!");
			break;
		case inches == "":
			document.getElementById("age").focus(); 
			alert("You must type something into all of the input boxes!!");
			break;
		case weight == "":
			document.getElementById("age").focus(); 
			alert("You must type something into all of the input boxes!!");
			break;
		case feet < 1: 
			document.getElementById("age").focus(); 
			alert("Your height cannot be more than 12 feet or less than 1 foot!!!")
			break; 
		case feet > 12: 
			document.getElementById("age").focus(); 
			alert("Your height cannot be more than 12 feet or less than 1 foot!!!")
			break; 			
		case inches < 1: 
			document.getElementById("age").focus(); 
			alert("The inches part of your height must be between 1 and 12 inches!!");
			break; 
		case inches > 12:
			document.getElementById("age").focus(); 
			alert("Your height cannot be more than 13 feet or less than 1 foot!!!")
			break; 
		default: 
			break; 
	}
}

