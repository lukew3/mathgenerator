
make:
	wasm-pack build --target web

wasi:
# rustup target add wasm32-wasi
	cargo build --target=wasm32-wasi

serve:
	python3 -m http.server