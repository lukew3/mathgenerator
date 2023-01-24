#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <emscripten.h>


// https://emscripten.org/docs/api_reference/val.h.html#_CPPv4N10emscripten10emscripten3val5arrayEv
EMSCRIPTEN_KEEPALIVE char* absolute_difference() {
    float rand_num = emscripten_random();
    char* prob = "prob";
    char* ans = "ans";
    sprintf(prob, "What is the absolute difference between %f and %f?", rand_num, rand_num);
    // std::vector<std::string> vec = {prob, ans};
    return prob;
}

int main() {
    return 0;
}
