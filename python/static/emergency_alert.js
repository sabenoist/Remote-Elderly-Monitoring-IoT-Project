$(document).ready(function() {
	var emergency_shown = false

	var chartFunction = function() {
		$.getJSON("http://127.0.0.1:5000/data/emergency/", function(emergency) {
	        if (parseInt(emergency) == 1 && !emergency_shown) {
	        	emergency_shown = true;
	        	document.getElementById("side_bar").style.backgroundColor = "#c80000";
	        	document.getElementById("alarm_image").style.visibility = "visible";
	        } else if (parseInt(emergency) == 0 && emergency_shown) {
	        	emergency_shown = false;
	        	document.getElementById("side_bar").style.backgroundColor = "#33a232";
	        	document.getElementById("alarm_image").style.visibility = "hidden";
	        } 
	    });
    };
    setInterval(chartFunction, 3000);
});