$(document).ready(function() {
	var d = new Date();
	document.getElementById("date").innerHTML = d.toDateString();

	var myVar = setInterval(myTimer, 1000);

	function myTimer() {
		var d = new Date();
		document.getElementById("time").innerHTML = d.toLocaleTimeString();
	}
});