
make:
	clang --target=wasm32-unknown-wasi --sysroot /tmp/wasi-libc \
  -O2 -s -o mathgenerator.wasm mathgenerator.cpp