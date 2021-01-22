
function submitButton() {
	var req = new XMLHttpRequest(); 
	var url = 'localhost:3000/insert?name=';

	if(document.getElementbyId('inputname').value != "") {
		url += document.getElementbyId('inputname').value;
	} else {
		return;
	}

	if(document.getElementbyId('inputreps').value != "") {
		url += '&reps=' + document.getElementbyId('inputreps').value;
	}

	if(document.getElementbyId('inputweight').value != "") {
		url += '&weight=' + document.getElementbyId('inputweight').value;
	}

	if(document.getElementbyId('inputdate').value != "") {
		url += '&date=' + document.getElementbyId('inputdate').value;
	}

	if(document.getElementbyId('pounds').checked) {
		url += '&units=0';
	} else if(document.getElementbyId('kilos').checked) {
		url += 'units=1';
	}
}

function deleteButton(c_row) {
	try {
		var cur_table = document.getElementById('workoutTable');
		var req = new XMLHttpRequest();
		var url = 'localhost:3000/delete?id='
	}
}