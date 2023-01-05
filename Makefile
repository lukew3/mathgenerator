
make:
	emcc mathgenerator.cpp -s WASM=1 -o mathgenerator.wasm --bind