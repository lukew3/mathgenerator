#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <vector>
#include <emscripten.h>
#include <emscripten/val.h>
#include <emscripten/bind.h>

using namespace emscripten;

// Use emscripten val to enable returning arrays
// https://emscripten.org/docs/api_reference/val.h.html#_CPPv4N10emscripten10emscripten3val5arrayEv
EMSCRIPTEN_KEEPALIVE std::vector<std::string> absolute_difference() {
    // float rand_num = emscripten_random();
    std::string prob = "prob";
    std::string ans = "ans";
    std::vector<std::string> vec = {prob, ans};
    return vec;
}

int main() {
    return 0;
}

EMSCRIPTEN_BINDINGS(module) {
    register_vector<std::string>("VectorString");
}