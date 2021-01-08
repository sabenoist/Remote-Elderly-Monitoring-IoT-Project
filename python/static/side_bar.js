$(document).ready(function() {
	$.getJSON("http://127.0.0.1:5000/data/gender/", function(gender) {
         $.getJSON("http://127.0.0.1:5000/data/name/", function(name) {
         	if (gender == 0) {
         		gender = "Mr. ";
         	} else {
         		gender = "Ms. ";
         	}

         	document.getElementById("name").innerHTML = gender.concat(name);
    	});
    });

    $.getJSON("http://127.0.0.1:5000/data/age/", function(age) {
    	var age_text = "Age: ";
    	document.getElementById("age").innerHTML = age_text.concat(age);
    });

	var d = new Date();
	document.getElementById("date").innerHTML = d.toDateString();

	var myVar = setInterval(myTimer, 1000);

	function myTimer() {
		var d = new Date();
		document.getElementById("time").innerHTML = d.toLocaleTimeString();
	}
});