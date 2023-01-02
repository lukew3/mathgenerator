#include <stdio.h>
#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE int square(int n) {
    return n*n;
}

EMSCRIPTEN_KEEPALIVE int add(int a, int b) {
    return a + b;
}

int main() {
    return 0;
}
