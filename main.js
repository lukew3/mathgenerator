for (let i=0; i<data.length-1; i++) {
	var div = document.createElement("DIV");
        div.className = "generatorListItem"
        div.innerHTML = "<p class='genListItem' onClick='setAg(" + data[i].id + ")'>" + data[i].name + "</p>";
        document.getElementById("generatorList").appendChild(div);
}
function setAg(id) {
	let gen = data[id];
        document.getElementById("agTitle").innerHTML = gen.name;
        document.getElementById("agFunctionName").innerHTML = gen.function_name;
        document.getElementById("agKwargs").innerHTML = gen.kwargs;
        document.getElementById("agId").innerHTML = gen.id;
        generateSample(id);
}
function generateSample(agId=-1) {
	if (agId==-1) agId = document.getElementById("agId").innerHTML;
        let sampleId = Math.floor((Math.random() * 10) + 1) - 1;
        let set = data[agId].samples[sampleId];
        document.getElementById("agProblem").innerHTML = set.problem;
        document.getElementById("agSolution").innerHTML = set.solution;
}
