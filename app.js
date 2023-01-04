const $ = (id) => document.getElementById(id);
const importObject = {
  wasi_snapshot_preview1: {
    proc_exit: (i) => console.log(i),
  },
};

(async function main() {
  const mathgenerator = (await WebAssembly.instantiateStreaming(fetch("mathgenerator.wasm"), importObject)).instance.exports

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
