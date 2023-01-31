const { init, WASI } = require('@wasmer/wasi');

const $ = (id) => document.getElementById(id);

async function main() {
  await init();

  let wasi = new WASI({
    env: {
        // 'ENVVAR1': '1',
        // 'ENVVAR2': '2'
    },
    args: [
        // 'command', 'arg1', 'arg2'
    ],
  });

  const moduleBytes = fetch("https://deno.land/x/wasm/tests/demo.wasm");
  const module = await WebAssembly.compileStreaming(moduleBytes);
  // Instantiate the WASI module
  await wasi.instantiate(module, {});

  // Run the start function
  console.log(wasi.exports.absolute_difference());
  let exitCode = wasi.start();
  let stdout = wasi.getStdoutString();

   // This should print "hello world (exit code: 0)"
  console.log(`${stdout}(exit code: ${exitCode})`);

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
};

main();

/*


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
    emscripten_memcpy_big: (dest, src, num) => HEAPU8.copyWithin(dest, src, src + num)
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

*/