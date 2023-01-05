
make:
	emcc mathgenerator.cpp -s WASM=1 -o mathgenerator.wasm --bind

js:
	emcc mathgenerator.cpp -s WASM=1 -o mathgenerator.js --bind

clang:
	clang mathgenerator.cpp --target=wasm32-unknown-wasi -o mathgenerator.wasm
