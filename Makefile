
make:
	emcc mathgenerator.c -o index.html

wasm-only:
	emcc mathgenerator.c -s WASM=1 -o mathgenerator.wasm