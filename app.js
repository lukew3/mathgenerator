const d_genList = document.getElementById("generatorList");
const d_id = document.getElementById("agId");
const d_title = document.getElementById("agTitle");
const d_funcName = document.getElementById("agFunctionName");
const d_subject = document.getElementById("agSubject");
const d_kwargs = document.getElementById("agKwargs");
const d_prob = document.getElementById("agProblem");
const d_sol = document.getElementById("agSolution");

for (let i=0; i<data.length-1; i++) {
	var div = document.createElement("DIV");
        div.className = "generatorListItem"
        div.innerHTML = "<p class='genListItem'>" + data[i].name + "</p>";
        d_genList.appendChild(div);
}
function setAg(id) {
	let gen = data[id];
    d_id.innerHTML = gen.id;
    d_title.innerHTML = gen.name;
    d_funcName.innerHTML = gen.function_name;
    d_subject.innerHTML = gen.subject
    //d_subject.innerHTML = gen.subject;
    d_kwargs.innerHTML = gen.kwargs.join(", ");
    generateSample(id);
}
function generateSample(agId=-1) {
	if (agId==-1) agId = document.getElementById("agId").innerHTML;
        let sampleId = Math.floor((Math.random() * 10) + 1) - 1;
        let set = data[agId].samples[sampleId];
        d_prob.innerHTML = set.problem;
        d_sol.innerHTML = set.solution;
}


let elements = document.getElementsByClassName("genListItem");
for(let i = 0; i < elements.length; i++) {
        elements[i].onclick = function () {
                setAg(data[i].id)
                if (window.innerWidth < 790) {
                        window.scrollTo(0, 0)
                }
        }
}