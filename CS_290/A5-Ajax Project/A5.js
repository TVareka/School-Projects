var apiKey = '916e1a8b12ee39106731b1099ad5a7ae';

bindButtons()

function bindButtons(){
	document.getElementById('citysubmit').addEventListener('click', function(event){
		var req = new XMLHttpRequest();
		var citycode = document.getElementById("city").value
		var countrycodec = document.getElementById("country").value
		if(isNaN(citycode)) {
			req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?q=' + citycode + ',' + countrycodec +'&appid=' + apiKey, true);
		}
		else {
			req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?zip=' + citycode + ',' + countrycodec +'&appid=' + apiKey, true);
		}
	    req.addEventListener('load',function(){
		if(req.status >= 200 && req.status < 400){
			var response = JSON.parse(req.responseText);
	    	document.getElementById('outputtext').textContent = JSON.stringify(response)
		} 
		else {
			console.log("Error in network request: " + req.statusText);
		}});
	    req.send(null);
	    event.preventDefault();
	})

	document.getElementById('postsubmit').addEventListener('click', function(event){
		var req = new XMLHttpRequest();
		req.open('POST', 'http://httpbin.org/post', true);
		req.setRequestHeader('Content-Type', 'application/json');
	    req.addEventListener('load',function(){
		if(req.status >= 200 && req.status < 400){
			var response = JSON.parse(req.responseText);
	    	document.getElementById('output').textContent = response.data;
		} 
		else {
			console.log("Error in network request: " + req.statusText);
		}});
	    req.send(document.getElementById('posttext').value);
	    event.preventDefault();
})}