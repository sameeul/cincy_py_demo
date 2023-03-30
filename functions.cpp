#include <vector>
#include <iostream>
#include <chrono>
#include <cmath>

#include "functions.h"


size_t calc_sum_of_squares(size_t n){
    std::vector<uint16_t> in_array(n,1);
    size_t sum = 0;
    for (size_t i=0;i<n; ++i){
        sum += in_array[i]*in_array[i];
    }

    return sum;
}

bool is_prime(size_t n){
    if (n==1) return false;
    if (n==2) return true;

    for(size_t i=2; i< ceil(sqrt(n)); i++){
        if (n%i == 0) return false;
    }

    return true;
}

size_t count_primes(size_t n){
    size_t count = 0;
    for(size_t i=1; i<=n; i++){
        if(is_prime(i)) count++;
    }

    return count;
}


