make:
	wasm-pack build --target web

clean:
	rm -r pkg

docs:
	cargo doc --target-dir .
