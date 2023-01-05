import * as mathgenerator from './pkg/mathgenerator.js';

const $ = (id) => document.getElementById(id);

(async function main() {
  console.log(mathgenerator);

  // This shouldn't be necessary right?
  mathgenerator.default();

  document.getElementById("testForm").addEventListener("submit", (e) => {
    e.preventDefault();
    let func = $('functionInput').value;
    let arg1 = $('arg1Input').value;
    let arg2 = $('arg2Input').value;
    if (func == '') {
      $('result').textContent = "Please provide a function";
    } else if (arg2 != "") {
      $('result').textContent = mathgenerator[func](Number(arg1), Number(arg2));
    } else if (arg1 != "") {
      $('result').textContent = mathgenerator[func](Number(arg1));
    } else {
      $('result').textContent = mathgenerator[func]();
    }
  })
})()