const $ = (id) => document.getElementById(id);

// This is a helper function to read a null-terminated string from C
let module;
const textDecoder = new TextDecoder();
const readStaticCString = (address) => {
  const buffer = module.instance.exports.memory.buffer;
  const encodedStringLength = (new Uint8Array(buffer, address)).indexOf(0);
  const encodedStringBuffer = new Uint8Array(buffer, address, encodedStringLength);
  return textDecoder.decode(encodedStringBuffer);
};

const importObject = {
  env: {
    emscripten_random: () => Math.random(),
  },
  wasi_snapshot_preview1: {
    proc_exit: (i) => console.log(i),
  },
};

(async function main() {
  module = await WebAssembly.instantiateStreaming(fetch("mathgenerator.wasm"), importObject);
  const mathgenerator = module.instance.exports
  console.log(mathgenerator);
  
  document.getElementById("testForm").addEventListener("submit", (e) => {
    e.preventDefault();
    let func = $('functionInput').value;
    let arg1 = $('arg1Input').value;
    let arg2 = $('arg2Input').value;
    if (func == '') {
      $('result').textContent = "Please provide a function";
    } else if (arg2 != "") {
      $('result').textContent = readStaticCString(mathgenerator[func](Number(arg1), Number(arg2)));
    } else if (arg1 != "") {
      $('result').textContent = readStaticCString(mathgenerator[func](Number(arg1)));
    } else {
      $('result').textContent = readStaticCString(mathgenerator[func]());
    }
  })
})()
