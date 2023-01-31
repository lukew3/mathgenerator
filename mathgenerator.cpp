#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Use emscripten val to enable returning arrays
// https://emscripten.org/docs/api_reference/val.h.html#_CPPv4N10emscripten10emscripten3val5arrayEv
int absolute_difference() {
    // float rand_num = emscripten_random();
    //std::string prob = "prob";
    //std::string ans = "ans";
    //std::vector<std::string> vec = {prob, ans};
    srand(time(0));
    int rand_num = rand();
    return rand_num;
}

int main() {
    return 0;
}
