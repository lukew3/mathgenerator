const d_id = document.getElementById("agId");
const d_title = document.getElementById("agTitle");
const d_func_name = document.getElementById("agFunctionName");
const d_subject = document.getElementById("agSubject");
const d_kwargs = document.getElementById("agKwargs");
const d_prob = document.getElementById("agProblem");
const d_sol = document.getElementById("agSolution");

let pyodide, genList, curId = 0;

async function generateSample() {
        let out = pyodide.runPython(`mathgenerator.genById(${curId})`)
        d_prob.innerHTML = out.get(0);
        d_sol.innerHTML = out.get(1);
}

async function setGenerator(id) {
        // Set global curId
        curId = id;
        // Set active generator text
        let g = genList.get(id);
        d_id.innerHTML = g.get(0);
        d_title.innerHTML = g.get(1);
        d_func_name.innerHTML = g.get(3);
        d_subject.innerHTML = g.get(4);
        d_kwargs.innerHTML = g.get(5).toString();
        // Move to top of screen if on mobile
        if (window.innerWidth < 790) window.scrollTo(0, 0);
        // Run generator
        generateSample();
}

(async () => {
        pyodide = await loadPyodide({
                indexURL : "https://cdn.jsdelivr.net/pyodide/v0.20.0/full/"
        });
        await pyodide.loadPackage("micropip");
        const micropip = pyodide.pyimport("micropip");
        await micropip.install('mathgenerator');
        await pyodide.runPython('import mathgenerator');
        // Build generator list
        genList = await pyodide.runPython('mathgenerator.getGenList()');
        for (let gen of genList) {
                var div = document.createElement("DIV");
                div.className = "generatorListItem"
                div.innerHTML = "<p class='genListItem'>" + gen.get(1) + "</p>";
                div.onclick = () => { setGenerator(gen.get(0)); };
                document.getElementById("generatorList").appendChild(div);
        }
})()
