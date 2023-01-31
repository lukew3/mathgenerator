
make:
<<<<<<< HEAD
	clang mathgenerator.c -o demo/mathgenerator.wasm

serve:
	cd demo && python3 -m http.server 8000
=======
	emcc mathgenerator.cpp -s WASM=1 -o mathgenerator.wasm --bind

js:
	emcc mathgenerator.cpp -s WASM=1 -o mathgenerator.js --bind

clang:
	clang mathgenerator.cpp --target=wasm32-unknown-wasi -o mathgenerator.wasm
>>>>>>> cfb09f498c22b852fabc64af45141370683fb89f
