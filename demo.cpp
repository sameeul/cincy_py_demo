#include <iostream>
#include <chrono>

#include "functions.h"

int main(){
    auto start_time = std::chrono::high_resolution_clock::now();
    //std::cout << "sum is " << calc_sum_of_squares(100000000)<<std::endl;
    auto count = count_primes(10000);
    auto end_time = std::chrono::high_resolution_clock::now();
    std::cout << count << " primes found" << std::endl;
    auto elapsed_time = end_time - start_time;
    std::cout << "elapsed time "<< std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_time).count()<<std::endl;

}
