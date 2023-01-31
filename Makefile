
make:
	clang mathgenerator.c -o demo/mathgenerator.wasm

serve:
	cd demo && python3 -m http.server 8000