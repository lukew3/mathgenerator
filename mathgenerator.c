#include <stdio.h>
#include <stdlib.h>
#include <time.h>


// https://emscripten.org/docs/api_reference/val.h.html#_CPPv4N10emscripten10emscripten3val5arrayEv
char* absolute_difference() {
    srand(time(NULL));
    int rand_num = rand();
    char* prob = "prob";
    char* ans = "ans";
    sprintf(prob, "What is the absolute difference between %d and %d?", rand_num, rand_num);
    // std::vector<std::string> vec = {prob, ans};
    return prob;
}

int main() {
    return 0;
}
