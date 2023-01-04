#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE float absolute_difference() {
    float rand_num = emscripten_random();
    return rand_num;
}

int main() {
    return 0;
}
