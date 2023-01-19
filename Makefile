
make:
	emcc mathgenerator.c -s WASM=1 -o mathgenerator.wasm

serve:
	python3 -m http.server 8000