/*
 * Define counter
 */

var pad = function(number){
	var str = ''+number;
	var myPad = '00'
	return myPad.substring(0, myPad.length - str.length) + str;
}

var myCounter = function(endingTime){

	var countdownType = countdown.HOURS | countdown.MINUTES | countdown.SECONDS;
	countdown.setLabels(
		null,
		null,
		null,
		null,
		'Now.');
	var timespan = countdown(endingTime,
		function(ts) {
			document.getElementById('remainingTime').innerHTML = ts.hours+":"+pad(ts.minutes)+":"+pad(ts.seconds);	
		},
		countdownType
		);

};

/**
 * Function to onclick close image
 */
var goHome = function(){
	window.location = "/";
}

/*
 * Start counter
 */

if (endingTime){
	myCounter(endingTime);	
}
