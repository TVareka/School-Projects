var currentCell = [1,1]; //[row, column]
var body = document.body;
var table = createTable();
body.appendChild(table);


function createTable()
{
	var table = document.createElement("table");
	var thead = document.createElement("thead");
	table.appendChild(thead);
	thead.appendChild(document.createElement("tr"));
	var trow = thead.children[0];

	for (var i=0; i<4; i++) { //OFF BY ONE ISSUE HERE**
		var heading = document.createElement("th");
		heading.id = "H" + (i);
		heading.textContent = "Header " + (i+1);
		heading.style.textAlign = "center";
		heading.style.borderStyle = "solid";
		heading.style.backgroundColor = "lightgreen";
		trow.appendChild(heading);
	}

	table.appendChild(document.createElement("tbody")); //FIX THIS
	var tbody = table.children[1];
	for (var i=0; i<3; i++) {
		var row = document.createElement("tr");

		for (var j=0; j<4; j++) {
			var section = document.createElement("td");
			section.id = "R" + (i+1) + "C" + (j+1);
			section.textContent = (i+1) + "," + (j+1);
			section.style.textAlign = "center";
			section.style.borderStyle = "solid";
			section.style.borderWidth = "2px";
			row.appendChild(section);
		}
		tbody.appendChild(row);
	}

	table.style.borderStyle = "solid";


	return table



}

// Element [0,0] needs to initialize with a thicker border 
document.getElementById("R1C1").style.borderWidth = "5px";

//Button Creation
var leftB = document.createElement("button");
leftB.id = "leftButton";
leftB.textContent = "left";
leftB.addEventListener("click", function() {
	buttonPress("left", currentCell);
});
body.appendChild(leftB);

var rightB = document.createElement("button");
rightB.id = "rightButton";
rightB.textContent = "right";
rightB.addEventListener("click", function() {
	buttonPress("right", currentCell);
});
body.appendChild(rightB);

var downB = document.createElement("button");
downB.id = "downButton";
downB.textContent = "down";
downB.addEventListener("click", function() {
	buttonPress("down", currentCell);
});
body.appendChild(downB);

var upB = document.createElement("button");
upB.id = "upButton";
upB.textContent = "up";
upB.addEventListener("click", function() {
	buttonPress("up", currentCell);
});
body.appendChild(upB);

var markB = document.createElement("button");
markB.id = "markButton";
markB.textContent = "MarkCell";
markB.addEventListener("click", function() {
	buttonPress("mark", currentCell);
});
body.appendChild(markB);

//Button Press Function
function buttonPress(dir, cell) 
{
	switch(dir) {
		case "left":
			if (cell[1] > 1) {
				document.getElementById("R" + cell[0] + "C" + cell[1]).style.borderWidth = "2px";
				cell[1]--; 
				document.getElementById("R" + cell[0] + "C" + cell[1]).style.borderWidth = "5px";
			}
			break;

		case "right":
			if (cell[1] < 4) {
				document.getElementById("R" + cell[0] + "C" + cell[1]).style.borderWidth = "2px";
				cell[1]++; 
				document.getElementById("R" + cell[0] + "C" + cell[1]).style.borderWidth = "5px";
			}
			break;

		case "down":
			if (cell[0] < 3) {
				document.getElementById("R" + cell[0] + "C" + cell[1]).style.borderWidth = "2px";
				cell[0]++; 
				document.getElementById("R" + cell[0] + "C" + cell[1]).style.borderWidth = "5px";
			}
			break;

		case "up":
			if (cell[0] > 1) {
				document.getElementById("R" + cell[0] + "C" + cell[1]).style.borderWidth = "2px";
				cell[0]--; 
				document.getElementById("R" + cell[0] + "C" + cell[1]).style.borderWidth = "5px";
			}
			break;

		case "mark":
			document.getElementById("R" + cell[0] + "C" + cell[1]).style.backgroundColor = "yellow";
			break;
	}

	return cell;
}
